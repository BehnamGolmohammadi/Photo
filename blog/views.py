from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def blog_home(request, **kwargs):
    if kwargs.get('cat') != None:
        posts= Post.objects.filter(Status = True, Category__Name = kwargs["cat"])
    else:
        if request.method == 'GET' and (search := request.GET.get('search')):
            posts = Post.objects.filter(Content__contains = search)
        else:
            posts= Post.objects.filter(Status = True)

    # get Categories
    Categories= Category.objects.all()[:10]

    # Pagination
    posts= Paginator(posts, 4)     # each page will have 4 posts
    page = request.GET.get('page')
    try:
        posts = posts.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver first page
        posts = posts.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of posts
        posts = posts.page(posts.num_pages)

    Context = {'posts': posts, 'category': Categories}
    return render(request, 'blog/blog.html', Context)

def blog_post(request, pid):
    post = Post.objects.get(Status = True, id = pid)
    Context = {'post': post}
    return render(request, 'blog/post.html', Context)

