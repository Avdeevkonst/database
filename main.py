import jinja2
from jinja2 import Template

per = "a href='#'>' 'link</a>"
a = jinja2.select_autoescape(per)

print(a)
