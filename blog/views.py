from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


# Create your views here.
def blog_home(request, **kwargs):
    if kwargs.get('cat') != None:
        posts= Post.objects.filter(Status = True, Category__Name = kwargs["cat"])
    else:
        posts= Post.objects.filter(Status = True)

    # get Categories
    Categories= Category.objects.all()[:10]
    Context = {'posts': posts, 'category': Categories}
    return render(request, 'blog/blog.html', Context)

def blog_post(request, pid):
    post = Post.objects.get(Status = True, id = pid)
    Context = {'post': post}
    return render(request, 'blog/post.html', Context)