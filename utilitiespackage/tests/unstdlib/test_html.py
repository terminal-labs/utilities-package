import os

from utilitiespackage.unstdlib.html import (
    _IMPORT_TIME,
    _BUST_METHODS,
    _cache_key_by_mtime,
    _cache_key_by_md5,
    tag_builder,
    tag,
    get_cache_buster,
    stylesheet_link,
    javascript_link,
)


def test_tag_builder():
    ul, li = tag_builder(["ul", "li"])
    assert ul(li(ch) for ch in "abc") == u"<ul><li>a</li><li>b</li><li>c</li></ul>"


def test_tag():
    assert tag("div", content="Hello, world.") == u"<div>Hello, world.</div>"
    assert tag("script", attrs={"src": "/static/js/core.js"}) == u'<script src="/static/js/core.js"></script>'
    assert tag("meta", content=None, attrs=dict(content='"quotedquotes"')) == u'<meta content="\\"quotedquotes\\"" />'
    assert tag("ul", (tag("li", str(i)) for i in range(3))) == u"<ul><li>0</li><li>1</li><li>2</li></ul>"


def test_get_cache_buster():
    SRC_PATH = os.path.join(os.path.dirname(__file__), "test_html.py")
    assert get_cache_buster(SRC_PATH) is _IMPORT_TIME
    assert get_cache_buster(SRC_PATH, method="mtime") == _cache_key_by_mtime(SRC_PATH)
    # assert get_cache_buster(SRC_PATH, method='md5') == _cache_key_by_md5(SRC_PATH)


def test_stylesheet_link():
    assert stylesheet_link("/static/css/media.css") == u'<link href="/static/css/media.css" rel="stylesheet"></link>'


def test_javascript_link():
    assert javascript_link("/static/js/core.js") == u'<script src="/static/js/core.js" type="text/javascript"></script>'
