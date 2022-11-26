from django import template
from blog.models import Post
register = template.Library()

# ------------- simple tags examplees ------------
@register.simple_tag
def hello(a):
    return f"hello {a}"
# -------------- change name of tags -------------
@register.simple_tag(name='plustwo')
def func(a):
    return a + 2

# -------------- get data from models with example of Post Model ---------------

@register.simple_tag(name = 'totalpost')
def T_post():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name = 'listpost')
def l_post():
    posts = Post.objects.filter(status = 1)
    return posts