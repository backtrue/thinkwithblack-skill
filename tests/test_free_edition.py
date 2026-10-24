import importlib.util,json,shutil,tempfile,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'scripts/build-free-edition.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class FreeEditionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.root=self.base/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def test_declared_dependency_must_exist(self):
        (self.root/'extensions/pmax-copy/references/copy-contract.md').unlink()
        with self.assertRaisesRegex(ValueError,'Missing source'):b.verify(self.root)
    def test_unlisted_method_cannot_be_shipped(self):
        p=self.root/'skills/not-public/SKILL.md';p.parent.mkdir();p.write_text('# Private')
        with self.assertRaisesRegex(ValueError,'inventory mismatch'):b.package(self.root,self.base/'out')
    def test_product_settings_cannot_be_shipped(self):
        (self.root/'.app.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'inventory mismatch'):b.verify(self.root)
    def test_changed_reference_requires_regeneration(self):
        p=self.root/'extensions/pmax-copy/references/copy-contract.md';p.write_text(p.read_text()+'\nChanged reference\n')
        with self.assertRaisesRegex(ValueError,'Stale generated file'):b.verify(self.root)
    def test_pack_has_no_unlisted_dependency(self):
        p=self.root/'skills/mk-001/SKILL.md';p.write_text(p.read_text()+'\n[extra](missing.md)\n')
        b.generate(self.root)
        with self.assertRaisesRegex(ValueError,'Broken local link'):b.verify(self.root)
    def test_path_cannot_escape_repository(self):
        p=self.root/'free-content.json';m=json.loads(p.read_text());m['entries'][0]['references']=['../outside.md'];p.write_text(json.dumps(m))
        with self.assertRaisesRegex(ValueError,'outside repository'):b.generate(self.root)
    def test_skill_description_and_index_cannot_drift(self):
        p=self.root/'free-content.json';m=json.loads(p.read_text())
        m['entries'][0]['description']='A different routing promise'
        p.write_text(json.dumps(m))
        with self.assertRaisesRegex(ValueError,'description/index mismatch'):b.generate(self.root)
    def test_missing_or_duplicate_discovery_metadata_is_rejected(self):
        p=self.root/'skills/mk-001/SKILL.md';original=p.read_text()
        for replacement in ['', 'name: mk-001\nname: another-name\n']:
            with self.subTest(replacement=replacement):
                p.write_text(original.replace('name: mk-001\n',replacement))
                with self.assertRaisesRegex(ValueError,'Missing or duplicate Skill name'):b.load(self.root)
    def test_skill_name_matches_its_directory(self):
        p=self.root/'skills/mk-001/SKILL.md';p.write_text(p.read_text().replace('name: mk-001','name: different-method'))
        with self.assertRaisesRegex(ValueError,'name/path mismatch'):b.load(self.root)
    def test_metadata_accepts_quoted_and_folded_descriptions(self):
        p=self.base/'SKILL.md'
        expected = 'A "quoted" description'
        for value in [json.dumps(expected), "'" + expected + "'", '>\n  A "quoted"\n  description']:
            p.write_text('---\nname: sample\ndescription: '+value+'\n---\n')
            self.assertEqual(b.skill_metadata(p)['description'],'A "quoted" description')
    def test_chinese_fragment_is_checked_before_packaging(self):
        p=self.root/'skills/mk-001/SKILL.md';p.write_text(p.read_text()+'\n[來源](#不存在的章節)\n')
        b.generate(self.root)
        with self.assertRaisesRegex(ValueError,'Broken local fragment'):b.package(self.root,self.base/'out')
    def test_reproducible_archives_and_same_content(self):
        r1=b.package(self.root,self.base/'one');r2=b.package(self.root,self.base/'two')
        self.assertEqual(r1,r2)
        names=list(r1['artifacts']);teaching=self.base/'one'/names[0];source=self.base/'one'/names[1]
        with zipfile.ZipFile(teaching) as t,zipfile.ZipFile(source) as s:
            for p,h in r1['files'].items():
                self.assertEqual(b.sha(t.read(p)),h);self.assertEqual(t.read(p),s.read(p))
            self.assertEqual(set(t.namelist()),set(r1['files']))
            self.assertIn('context/CASE_CONTEXT.template.md',t.namelist())
            self.assertIn('examples/consultant-decisions.md',t.namelist())
            self.assertIn('Copyright (c) 2025 Corey Haines',t.read('packs/write-marketing-rollout-plan.md').decode())
            self.assertIn('wang.joan.888',t.read('README.md').decode())
            self.assertNotIn('.git',s.namelist())
    def test_required_examples_and_cross_topic_route(self):
        m,out=b.verify(self.root);ids={e['id'] for e in m['entries']}
        self.assertTrue({'MK-001','MK-059','MK-390','INF-05-07'}<=ids)
        self.assertNotIn('MK-452',ids)
        self.assertIn('索引只',out['INDEX.md'].decode())
        for name in ['mk-001','mk-059','mk-390']:
            text=out['packs/'+name+'.md'].decode()
            self.assertIn('重新查索引',text);self.assertIn('## 方法步驟',text);self.assertIn('## 方法來源',text)
    def test_supplement_keeps_the_complete_article_and_has_no_file_dependencies(self):
        manifest,out=b.verify(self.root)
        self.assertEqual(len(manifest['entries']),365)
        supplement=manifest['supplements'][0]
        sample=(self.root/'supplements/speak-human-tw/references/long-form-approved-example.md').read_text().strip()
        pack=out[supplement['pack']].decode()
        self.assertIn(sample,pack)
        self.assertIn('(#supplement-reference-',pack)
        self.assertIn('speak-human-tw',out['INDEX.md'].decode())
        catalog=json.loads(out['catalog.json'])
        self.assertEqual(catalog['supplements'][0]['sourceSha256'],b.sha((self.root/supplement['source']).read_bytes()))
    def test_interest_pack_keeps_guide_without_redistributing_datasets(self):
        for language in ['', 'en/']:
            manifest=json.loads((self.root/(language+'free-content.json')).read_text())
            entry=next(e for e in manifest['entries'] if e['id']=='MK-164')
            self.assertEqual(entry['references'],['skills/mk-164/assets/interest-reference.md','skills/mk-164/assets/context-contract.json','skills/mk-164/assets/check-context.py'])
            pack=(self.root/(language+entry['pack'])).read_text()
            self.assertIn('https://www.eachspy.com/terms/',pack)
            self.assertIn('https://primenumbers.co.jp/download/meta_interesting/',pack)
            self.assertNotIn('eachspy-302-interests.csv',pack)
            self.assertNotIn('primenumbers-interests.csv',pack)
            self.assertNotIn('Advertising,466M',pack)
    def test_supplement_missing_reference_is_rejected(self):
        (self.root/'supplements/speak-human-tw/references/long-form-approved-example.md').unlink()
        with self.assertRaisesRegex(ValueError,'Missing supplemental source'):b.verify(self.root)
    def test_original_language_supplement_cannot_drift_in_english_download(self):
        p=self.root/'en/supplements/speak-human-tw/references/long-form-approved-example.md'
        p.write_text(p.read_text()+'\nChanged example\n')
        with self.assertRaisesRegex(ValueError,'Source-language supplement differs'):b.verify(self.root)
if __name__=='__main__':unittest.main()
