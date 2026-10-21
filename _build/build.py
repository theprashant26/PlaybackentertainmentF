"""Build the static site.

Usage (from the project root):  python _build/build.py

Writes every page to <slug>/index.html so URLs match the handover sitemap
(/about-us/, /corporate-photography/, /portfolio/<project>/ ...), plus
sitemap.xml, robots.txt and 404.html. Content lives in data.py, services.py,
blog.py and pages.py; layout and components live in core.py.
"""
import os, sys, shutil, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import pages, services
from data import PROJECTS, SITE, PREVIEW
from blog import POSTS
from core import render

# Folders the build owns (cleaned before writing, so removed pages disappear)
def generated_dirs(outputs):
    return sorted({p.split('/')[0] for p, _ in outputs if p and p != '404/'})

def write(path, html_):
    full = os.path.join(ROOT, path, 'index.html') if path else os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html_)

def main():
    outputs = [
        pages.home(), pages.about(), pages.team_page(), pages.services_hub(), pages.portfolio(), pages.showreel(),
        pages.clients_page(), pages.blog_index(), pages.careers(), pages.freelancers(), pages.contact_page(), pages.quote_page(),
        pages.legal('privacy-policy', 'Privacy Policy', pages.PRIVACY), pages.legal('terms-conditions', 'Terms &amp; Conditions', pages.TERMS),
    ]
    outputs += services.render_all()
    outputs += [pages.project_page(p, i) for i, p in enumerate(PROJECTS)]
    outputs += [pages.post_page(p) for p in POSTS]

    for d in generated_dirs(outputs):
        target = os.path.join(ROOT, d)
        if os.path.isdir(target) and d not in ('assets', '_build'):
            shutil.rmtree(target)
    for path, html_ in outputs:
        write(path, html_)

    # 404 (GitHub Pages serves it at any depth, so resolve links from the site root)
    _, nf = pages.not_found()
    nf = nf.replace('"../"', '"./"').replace('../', '')
    base = ("<script>(function(){var b=location.pathname.indexOf('/PlaybackentertainmentF/')===0?'/PlaybackentertainmentF/':'/';"
            "document.write('<base href=\"'+b+'\">');})();</script>")
    nf = nf.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  ' + base, 1)
    with open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(nf)

    # sitemap & robots
    today = dt.date.today().isoformat()
    urls = [p for p, _ in outputs]
    pri = lambda p: '1.0' if p == '' else ('0.9' if p.count('/') == 1 and not p.startswith(('portfolio/', 'blog/')) else '0.7')
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append(f'  <url><loc>{SITE["url"]}/{p}</loc><lastmod>{today}</lastmod><priority>{pri(p)}</priority></url>')
    sm.append('</urlset>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(sm) + '\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n') as f:
        if PREVIEW:
            f.write('# Design preview: not for indexing. Set PREVIEW = False in _build/data.py for launch.\nUser-agent: *\nDisallow: /\n')
        else:
            f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE["url"]}/sitemap.xml\n')

    print('PREVIEW mode: noindex on every page, robots.txt blocks crawlers' if PREVIEW else 'LIVE mode: pages are indexable')
    print(f'Built {len(outputs)} pages + 404.html, sitemap.xml ({len(urls)} URLs), robots.txt')

if __name__ == '__main__':
    main()
