from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def blog_home(request):
    posts= Post.objects.filter(Status = True)
    Context = {'posts': posts}
    return render(request, 'blog/blog.html', Context)

def blog_post(request, pid):
    post = Post.objects.get(Status = True, id = pid)
    Context = {'post': post}
    return render(request, 'blog/post.html', Context)