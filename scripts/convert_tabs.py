#!/usr/bin/env python3
"""Convert literal tabs to 4 spaces for common text file types.

Usage:
  python scripts/convert_tabs.py [root_path]

Creates a .bak copy for each modified file before overwriting.
"""
from pathlib import Path
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
EXTS = {'.py', '.html', '.htm', '.css', '.js', '.json', '.md', '.txt'}
EXCLUDE_NAMES = {'Makefile'}
TAB = ' ' * 4

def convert_file(p: Path):
    try:
        text = p.read_text(encoding='utf-8')
    except Exception:
        return False
    if '\t' not in text:
        return False
    backup = p.with_suffix(p.suffix + '.bak')
    backup.write_text(text, encoding='utf-8')
    new = text.replace('\t', TAB)
    p.write_text(new, encoding='utf-8')
    return True

def main():
    changed = 0
    for p in ROOT.rglob('*'):
        if not p.is_file():
            continue
        if p.name in EXCLUDE_NAMES:
            continue
        if p.suffix.lower() in EXTS:
            if convert_file(p):
                print('Converted', p)
                changed += 1
    print(f'Done. Files changed: {changed}')

if __name__ == '__main__':
    main()
