import os
import re
import yaml
import shutil
from glob import glob
from nom.md2html import compile_markdown
from jinja2 import FileSystemLoader, environment

BUILD_DIR = '.build'
META_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)

dir = os.path.dirname(os.path.abspath(__file__))
templ_dir = os.path.join(dir, 'templates')
env = environment.Environment()
env.loader = FileSystemLoader(templ_dir)


def extract_metadata(raw):
    meta_match = META_RE.search(raw)
    if meta_match is not None:
        meta_raw = meta_match.group(1)
        try:
            meta = yaml.load(meta_raw)

            # remove the metadata before we compile
            raw = META_RE.sub('', raw).strip()
        except yaml.scanner.ScannerError:
            pass
    return raw, meta

def strip_p(html):
    return html.replace('<p>', '').replace('</p>', '')

def process_metadata(meta):
    for k, v in meta.items():
        if isinstance(v, list):
            meta[k] = [strip_p(compile_markdown(i)) for i in v]
        elif isinstance(v, str):
            meta[k] = strip_p(compile_markdown(v))
    return meta

def prep_build_dir():
    if not os.path.isdir(BUILD_DIR):
        os.mkdir(BUILD_DIR)
    for f in os.listdir(BUILD_DIR):
        fpath = os.path.join(BUILD_DIR, f)
        if os.path.isfile(fpath):
            os.remove(fpath)
        elif os.path.isdir(fpath):
            shutil.rmtree(fpath)

if __name__ == '__main__':
    prep_build_dir()

    # project pages
    for md in glob('projects/*.md'):
        fname = os.path.basename(md)[:-3]
        raw = open(md, 'r').read()
        raw, meta = extract_metadata(raw)
        meta = process_metadata(meta)
        html = compile_markdown(raw)
        templ = env.get_template('project.html')
        html = templ.render(meta=meta, html=html)

        outdir = os.path.join(BUILD_DIR, fname)
        os.mkdir(outdir)
        with open(os.path.join(outdir, 'index.html'), 'w') as f:
            f.write(html)

    # index page
    templ = env.get_template('index.html')
    meta = yaml.load(open('meta.yaml', 'r'))
    projects = yaml.load(open('projects.yaml', 'r'))
    stalled = yaml.load(open('stalled.yaml', 'r'))
    html = templ.render(projects=projects, stalled=stalled, meta=meta)
    with open(os.path.join(BUILD_DIR, 'index.html'), 'w') as f:
        f.write(html)

    # assets etc
    for d in ['assets', 'css', 'favicon.ico']:
        if os.path.isdir(d):
            shutil.copytree(d, '.build/{}'.format(d))
        else:
            shutil.copy(d, '.build/{}'.format(d))
