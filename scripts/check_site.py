"""Check generated pages for missing assets, links, anchors and basic structure."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / '_site'
EXPECTED = {'index.html', 'researchers.html', 'participants.html', 'legal.html', 'policy.html'}

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.tags = path, set(), [], []
        self.h1 = 0
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == 'h1':
            self.h1 += 1
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


def check():
    files = {p.name for p in ROOT.glob('*.html')}
    assert files == EXPECTED, f'Expected five pages, found: {files}'
    pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
    count = 0
    for path, page in pages.items():
        assert page.h1 == 1, f'{path.name}: expected exactly one h1'
        assert all(t in page.tags for t in ('title', 'main', 'nav', 'footer')), path.name
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert target.is_relative_to(ROOT.resolve()), f'Link leaves site: {link}'
            assert target.exists(), f'{path.name}: missing target {link}'
            if parsed.fragment and target in pages:
                assert unquote(parsed.fragment) in pages[target].ids, f'{path.name}: missing anchor {link}'
            count += 1
    print(f'Checked {len(pages)} pages and {count} local links/assets/anchors.')

if __name__ == '__main__':
    check()
