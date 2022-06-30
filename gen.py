#!/usr/bin/env python3
import os
from pathlib import Path
from page.gen import generate_site

ROOT = str(Path(os.getcwd()).parent)
SOURCE = os.path.join(ROOT, 'blocl-pages/')
TARGET = os.path.join(ROOT, 'blocl/static')
TPL = os.path.join(ROOT, 'blocl/blocl/templates')
EXT = ''  # can be '.htm'/'.html'
CTX = dict(
    site_name='Blocl',
    site_url='https://blocl.uk',
    repo_url='https://github.com/fmalina/blocl-pages/blob/main/',  # for edit links
    dev=False  # show/hide editing links
)

if __name__ == '__main__':
    generate_site(SOURCE, TARGET, TPL, EXT, CTX)
