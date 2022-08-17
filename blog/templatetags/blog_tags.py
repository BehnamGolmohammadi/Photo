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

@register.inclusion_tag('website/Website-Album.html')
def Album():
    posts= Post.objects.filter(Status = True).order_by('-Published_Date')
    categories = Category.objects.all()
    Category_Dict= dict()

    for category in categories:
        Category_Dict[category] = list(posts.filter(Category = category))[:12]
    Category_Dict = dict(sorted(Category_Dict.items(), key=lambda item: -len(item[1]))[:9])
    Context = {'Category_Dict': Category_Dict}
    return Context