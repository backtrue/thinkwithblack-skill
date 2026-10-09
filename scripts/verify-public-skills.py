#!/usr/bin/env python3
"""Validate public content, dependency closure and generated artifacts."""
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name('build-free-edition.py')))
catalog,_=m['verify'](m['ROOT'])
print('PASS:',len(catalog['entries']),'free methods, references, packs and index')
