#!/usr/bin/env python3
"""Generate and verify the complete English edition against its Chinese sources."""
from pathlib import Path
import argparse
import importlib.util
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('free_builder', ROOT / 'scripts/build-free-edition.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def source_paths(manifest):
    return set(core.source_files(manifest))


def load(root):
    english = root / 'en'
    manifest = core.load(english)
    original = core.load(root)
    if manifest.get('language') != 'en':
        raise ValueError('English manifest language must be en')
    if manifest.get('sourceVersion') != original['version']:
        raise ValueError('English source version is stale')
    before = {e['id']: e for e in original['entries']}
    after = {e['id']: e for e in manifest['entries']}
    if before.keys() != after.keys():
        raise ValueError('English method inventory mismatch')
    for identifier, entry in after.items():
        for key in ['source', 'pack', 'references']:
            if entry[key] != before[identifier][key]:
                raise ValueError('English method mapping mismatch: ' + identifier + ': ' + key)
        for key in ['name', 'description']:
            if not entry[key].strip() or re.search(r'[\u3400-\u9fff]', entry[key]):
                raise ValueError('Untranslated English metadata: ' + identifier + ': ' + key)
    if manifest.get('supplements',[]) != original.get('supplements',[]):
        raise ValueError('Source-language supplement inventory mismatch')
    for entry in manifest.get('supplements',[]):
        for rel in [entry['source']]+entry['references']:
            if core.safe(root,rel).read_bytes()!=core.safe(english,rel).read_bytes():
                raise ValueError('Source-language supplement differs: '+rel)
    return manifest


def render_pack(root, entry, version):
    english = root / 'en'
    refs = entry['references']
    anchors = {(english / p).resolve(): 'reference-' + str(i) for i, p in enumerate(refs, 1)}

    def render(rel):
        text = (english / rel).read_text()
        if rel == entry['source']:
            text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
            # Sources may point readers to the upload pack; the pack already is that file
            text = re.sub(r'^.*`packs/[a-z0-9-]+\.md`.*\n', '', text, count=1, flags=re.M)

        def replace(match):
            target = core.local_link(english, rel, match[1])
            if target in anchors:
                return match[0].replace('(' + match[1] + ')', '(#' + anchors[target] + ')')
            if target == (english / 'PUBLIC_SKILL_RULES.md').resolve():
                return '[Shared rules](#common-rules)'
            return match[0]

        text = core.LINK.sub(replace, text)
        for dep in refs:
            relative = str(Path(dep).relative_to(Path(entry['source']).parent))
            if relative in text:
                text = text.replace(relative, '[Appendix: ' + Path(dep).name + '](#' + anchors[(english / dep).resolve()] + ')')
        return text.strip()

    chunks = [
        f'# {entry["id"]} | {entry["name"]} — method pack\n\nMaterials version: {version}',
        '<a id="common-rules"></a>\n\n' + (english / 'PUBLIC_SKILL_RULES.md').read_text().strip(),
        render(entry['source']),
    ]
    for rel in refs:
        body = (english / rel).read_text().strip()
        body = '```csv\n' + body + '\n```' if rel.endswith('.csv') else render(rel)
        chunks.append(f'<a id="{anchors[(english / rel).resolve()]}"></a>\n\n## Appendix: {Path(rel).name}\n\n' + body)
    chunks.append('## Materials license\n\n' + (english / 'LICENSE').read_text().strip())
    return ('\n\n'.join(chunks) + '\n').encode()


def expected(root):
    manifest = load(root)
    english = root / 'en'
    generated = {}
    entries = []
    for entry in manifest['entries']:
        pack = render_pack(root, entry, manifest['version'])
        generated[entry['pack']] = pack
        entries.append({**entry, 'sourceSha256': core.sha((english / entry['source']).read_bytes()),
                        'packSha256': core.sha(pack),
                        'referenceSha256': {p: core.sha((english / p).read_bytes()) for p in entry['references']}})
    catalog = {'schemaVersion': '2.0', 'edition': 'free', 'language': 'en',
               'version': manifest['version'], 'sourceVersion': manifest['sourceVersion'],
               'entryCount': len(entries), 'entries': entries}
    if manifest.get('supplements'):
        catalog['supplements']=[]
        for entry in manifest['supplements']:
            pack=core.render_supplement(english,entry,manifest['version'])
            generated[entry['pack']]=pack
            catalog['supplements'].append({**entry,'sourceSha256':core.sha((english/entry['source']).read_bytes()),'packSha256':core.sha(pack),'referenceSha256':{p:core.sha((english/p).read_bytes()) for p in entry['references']}})
    generated['catalog.json'] = (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode()
    index = f'''# ThinkWithBlack free method index

Materials version: {manifest['version']} | {len(entries)} methods | Language: English
Chinese source version: {manifest['sourceVersion']}

## Read this first

This index is for selecting a method. Whenever the user asks a question or changes tasks, choose one method that can fully address the current work. State its ID, name and full method-pack path from the table. If you have not read that method's complete text, ask the user to upload it before proceeding. Do not replace the method with its index summary

Reuse the complete method when the same version has already been read and it fits the task. Do not ask again for background when the user adds or corrects data. When another task needs a different method, check this index again and request that file. For multiple independent tasks, ask the user to choose one first. If no method fits, say so without inventing a method or filename

Use the files uploaded in this conversation and the specified readable sources to complete the single task, then wait for the next question. Account connections, overall diagnosis and automatic follow-through, continuous monitoring and operations in external systems are handled through ThinkWithBlack MCP product services

Each method pack includes the shared rules, complete method, required references and license. Paths below are relative to the English materials directory. In a bilingual checkout, use the files under `en/`

| ID | Method | When to use it | File to upload |
|---|---|---|---|
'''
    for entry in entries:
        desc = entry['description'].replace('|', '/').replace('\n', ' ')
        name = entry['name'].replace('|', '/')
        index += f'| {entry["id"]} | {name} | {desc} | [{entry["pack"]}]({entry["pack"]}) |\n'
    if manifest.get('supplements'):
        index+='\n## Source-language editing supplements\n\n'
        for entry in manifest['supplements']:
            index+=f'- [{entry["id"]}: Traditional Chinese editing helper]({entry["pack"]}) — includes the complete original-language writing example\n'
    generated['INDEX.md'] = index.encode()
    return manifest, generated


def paths(root):
    manifest, generated = expected(root)
    return source_paths(manifest) | set(generated) | {'TRANSLATION.json'}


def verify_provenance(root, manifest):
    english = root / 'en'
    record = json.loads((english / 'TRANSLATION.json').read_text())
    original = core.load(root)
    if record.get('language') != 'en' or record.get('version') != manifest['version'] or record.get('sourceVersion') != original['version']:
        raise ValueError('English translation version record mismatch')
    for key, base, required in [('sourceFiles', root, source_paths(original)),
                                ('translatedFiles', english, source_paths(manifest))]:
        hashes = record.get(key, {})
        if set(hashes) != required:
            raise ValueError('English translation hash inventory mismatch: ' + key)
        for rel, digest in hashes.items():
            if core.sha(core.safe(base, rel).read_bytes()) != digest:
                raise ValueError('English translation review required: ' + key + ': ' + rel)


def language_exceptions(root):
    # Preserve identifiable original titles and source dataset labels, not prose
    allowed = {'繁體中文', '邱煜庭', '小黑老師', '網路行銷零元本舖',
               '網路集客力：從 SEO 到 Facebook 的行銷新方略', '蘿琳亞'}
    for entry in core.load(root)['entries']:
        for line in (root / entry['source']).read_text().splitlines():
            if line.startswith('原始檔：'):
                allowed.add(line.removeprefix('原始檔：').strip())
    source_rows = (root / 'skills/mk-164/assets/primenumbers-interests.csv').read_text().splitlines()[2:]
    return sorted(allowed, key=len, reverse=True), source_rows


def verify_language(rel, text, exceptions):
    titles, source_rows = exceptions
    if rel in {'skills/mk-164/assets/primenumbers-interests.csv',
               'skills/mk-164/assets/interest-reference.md', 'packs/mk-164.md'}:
        # These rows are original Japanese category/interest labels used as evidence
        retained = set(source_rows)
        text = '\n'.join(line for line in text.splitlines() if line not in retained)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\]\([^\n)]*\)', ']', text)
    text = re.sub(r'https?://\S+', '', text)
    for title in titles:
        text = text.replace(title, '')
    if re.search(r'[\u3400-\u9fff]', text):
        raise ValueError('Untranslated English content: ' + rel)


def markdown_anchors(text):
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.M):
        heading = re.sub(r'<[^>]+>', '', heading).strip().lower()
        heading = re.sub(r'[^\w\s-]', '', heading)
        anchor = re.sub(r'\s', '-', heading)
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        anchors.add(anchor + ('-' + str(count) if count else ''))
    return anchors


def verify_fragments(english, rel, text):
    for match in core.LINK.finditer(text):
        link = unquote(match[1].strip('<>'))
        if '#' not in link or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', link):
            continue
        path, fragment = link.split('#', 1)
        target = core.local_link(english, rel, path) if path else english / rel
        if fragment and target and target.is_file() and target.suffix == '.md':
            if fragment not in markdown_anchors(target.read_text()):
                raise ValueError('Broken English fragment in ' + rel + ': ' + link)


def verify(root):
    manifest, generated = expected(root)
    english = root / 'en'
    wanted = source_paths(manifest) | set(generated) | {'TRANSLATION.json'}
    actual = {str(p.relative_to(english)) for p in english.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    if actual != wanted:
        raise ValueError('English file inventory mismatch: ' + str(sorted(actual ^ wanted)))
    verify_provenance(root, manifest)
    for rel, data in generated.items():
        if (english / rel).read_bytes() != data:
            raise ValueError('Stale English generated file: ' + rel)
    exceptions = language_exceptions(root)
    original_language_files={p for entry in manifest.get('supplements',[]) for p in [entry['source'],entry['pack']]+entry['references']}
    for rel in sorted(wanted):
        path = core.safe(english, rel)
        text = path.read_text()
        for pattern in core.PRODUCT_PATTERNS:
            if re.search(pattern, text):
                raise ValueError('Product content in English file: ' + rel + ': ' + pattern)
        if rel.endswith(('.md', '.csv')) and rel not in original_language_files:
            verify_language(rel, text, exceptions)
        if rel.endswith('.md'):
            verify_fragments(english, rel, text)
            for match in core.LINK.finditer(text):
                target = core.local_link(english, rel, match[1])
                if target and not target.is_file():
                    raise ValueError('Broken English local link in ' + rel + ': ' + match[1])
                if rel.startswith('packs/') and target:
                    raise ValueError('English pack has external file dependency: ' + rel)
    return manifest, generated


def generate(root):
    manifest, generated = expected(root)
    for rel, data in generated.items():
        path = root / 'en' / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['generate', 'verify'])
    args = parser.parse_args()
    if args.action == 'generate':
        manifest = generate(ROOT)
        print('Generated', len(manifest['entries']), 'English packs')
    else:
        manifest, _ = verify(ROOT)
        print('PASS:', len(manifest['entries']), 'English methods, references, packs, index and source mappings')
