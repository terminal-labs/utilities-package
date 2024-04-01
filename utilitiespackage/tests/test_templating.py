from utilitiespackage.templating import render_genshi_template_to_xhtml


def test_render_genshi_template_to_xhtml():
    template_data = """<h1>Hello, ${context['word']}!</h1>"""
    assert render_genshi_template_to_xhtml(template_data, {"word": "world"}) == "<h1>Hello, world!</h1>"
