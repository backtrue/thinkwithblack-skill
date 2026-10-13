# Versions and maintenance

## Get and update the materials

The version appears in `INDEX.md` and `catalog.json`. English methods have the same IDs as their Chinese counterparts. The English manifest records both the English edition version and its Chinese source version; `TRANSLATION.json` records the exact source files reviewed

Use the index and packs from the same language and version. Upload the updated pack when an existing conversation needs a revised method

## Maintainer commands

Use Python 3.10 or newer. The build uses the standard library. Run these commands from the bilingual source repository root

```sh
python3 scripts/build-free-edition.py generate
python3 scripts/verify-public-skills.py
python3 -m unittest discover -s tests
python3 scripts/build-free-edition.py package --output /absolute/output/directory
```

The root `free-content.json` defines the Chinese public collection. `en/free-content.json` mirrors those IDs, source paths and references with English names and descriptions. Sources, required references and each language's `PUBLIC_SKILL_RULES.md` produce its index, self-contained packs and catalog

When a Chinese source changes, review and update its English counterpart. After that review, refresh the affected hashes in `en/TRANSLATION.json`. Generation does not silently mark changed Chinese sources as translated. Verification checks the source-version record and catches files that changed without a corresponding review

Packaging verifies content, then creates a bilingual materials ZIP, a source ZIP and a standalone English materials ZIP with per-file hashes in the receipt. Distribute the same artifact at each download location and check its version and SHA-256 hash

Before publication, check that the Git history, attachments and downloadable files all match the public content scope. The source ZIP contains the complete bilingual sources and build tools
