from django import template

from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-LatestPosts.html')
def LatestPosts():
    posts= Post.objects.filter(Status = True).order_by('-Published_Date')[:4]
    Context = {'posts': posts}
    return Context

@register.filter
def Shorter_Content(Content, UpTo = 10):
    return ' '.join(Content.split()[:UpTo]) + ' ...'