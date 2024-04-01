from string import Template
from genshi.template import MarkupTemplate


def render_genshi_template_to_xhtml(template_data, context, minify=False):
    tmpl = MarkupTemplate(template_data)
    stream = tmpl.generate(context=context)
    xhtml = stream.render("xhtml")
    return xhtml


def render_simple_template(template_data, context):
    src = Template(template_data)
    result = src.substitute(context)
    return result
