import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('english', ROOT / 'scripts/build-english-edition.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
b = e.core


class EnglishEditionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.root = self.base / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def test_all_methods_and_references_have_english_counterparts(self):
        original = b.load(self.root)
        translated, generated = e.verify(self.root)
        self.assertEqual(len(original['entries']), len(translated['entries']))
        self.assertEqual({x['id'] for x in original['entries']}, {x['id'] for x in translated['entries']})
        for item in translated['entries']:
            self.assertIn(item['pack'], generated)
            for path in [item['source']] + item['references']:
                self.assertTrue((self.root / 'en' / path).is_file())
        # Packs can be uploaded alone, with reference text and licenses embedded
        self.assertIn(b'Copyright (c) 2025 Corey Haines', generated['packs/write-marketing-rollout-plan.md'])

    def test_missing_english_method_cannot_be_packaged(self):
        (self.root / 'en/skills/mk-001/SKILL.md').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing source'):
            b.package(self.root, self.base / 'out')

    def test_changed_chinese_source_requires_translation_review(self):
        path = self.root / 'skills/mk-001/SKILL.md'
        path.write_text(path.read_text() + '\nChanged source requirement\n')
        b.generate(self.root)
        with self.assertRaisesRegex(ValueError, 'translation review required: sourceFiles'):
            b.verify(self.root)

    def test_regeneration_does_not_approve_changed_translation(self):
        path = self.root / 'en/skills/mk-001/SKILL.md'
        path.write_text(path.read_text() + '\nChanged translation\n')
        b.generate(self.root)
        with self.assertRaisesRegex(ValueError, 'translation review required: translatedFiles'):
            b.verify(self.root)

    def test_removing_method_from_english_manifest_is_rejected(self):
        path = self.root / 'en/free-content.json'
        manifest = json.loads(path.read_text())
        removed = manifest['entries'].pop(0)
        path.write_text(json.dumps(manifest))
        (self.root / 'en' / removed['source']).unlink()
        with self.assertRaisesRegex(ValueError, 'English method inventory mismatch'):
            e.generate(self.root)

    def test_stale_english_pack_is_rejected(self):
        path = self.root / 'en/packs/mk-001.md'
        path.write_text(path.read_text() + '\nStale generated text\n')
        with self.assertRaisesRegex(ValueError, 'Stale English generated file'):
            b.verify(self.root)

    def test_untranslated_body_is_rejected(self):
        text = (self.root / 'en/skills/mk-001/SKILL.md').read_text()
        with self.assertRaisesRegex(ValueError, 'Untranslated English content'):
            e.verify_language('skills/mk-001/SKILL.md', text + '\n這段方法尚未翻譯\n', e.language_exceptions(self.root))

    def test_broken_local_section_link_is_rejected(self):
        text = (self.root / 'en/README.md').read_text().replace('#start-your-first-task', '#missing-section')
        with self.assertRaisesRegex(ValueError, 'Broken English fragment'):
            e.verify_fragments(self.root / 'en', 'README.md', text)

    def test_english_only_zip_is_complete_and_reproducible(self):
        one = b.package(self.root, self.base / 'one')
        two = b.package(self.root, self.base / 'two')
        self.assertEqual(one, two)
        name = next(name for name, meta in one['artifacts'].items() if meta.get('language') == 'en')
        with zipfile.ZipFile(self.base / 'one' / name) as archive:
            self.assertEqual(set(archive.namelist()), e.paths(self.root))
            manifest = e.load(self.root)
            self.assertEqual(len(manifest['entries']), 365)
            self.assertEqual({p for p in archive.namelist() if p.startswith('packs/')},
                             {entry['pack'] for entry in manifest['entries'] + manifest.get('supplements', [])})
            self.assertIn('Read the attached INDEX.md', archive.read('README.md').decode())
            self.assertNotIn('en/INDEX.md', archive.namelist())
            for path in archive.namelist():
                self.assertEqual(archive.read(path), (self.root / 'en' / path).read_bytes())


if __name__ == '__main__':
    unittest.main()
