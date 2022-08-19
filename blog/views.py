from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def blog_home(request, **kwargs):
    if kwargs.get('cat') != None:
        posts= Post.objects.filter(Status = True, Category__Name = kwargs["cat"])
    else:
        if request.method == 'GET' and (search := request.GET.get('search')):
            posts = Post.objects.filter(Content__contains = search)
        else:
            Local_Time = timezone.localtime(timezone.now())
            posts= Post.objects.filter(Published_Date__lte = Local_Time).order_by('-Published_Date')
            for post in posts:
                if not post.Status: post.Status = True
                post.save()

    # get Categories
    Categories= Category.objects.all()[:10]

    # Pagination
    posts= Paginator(posts, 3)     # each page will have 3 posts
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
    if request.method == 'POST':
        Form = CommentForm(request.POST, request.FILES)
        print(Form)
        if Form.is_valid():
            try:
                Form.save()
                msg = 'Your Comment submitted and will shown after we check it.'
                messages.success(request, msg)
                return redirect('/')
            except:
                msg = 'Your Comment did not submitted!'
                messages.error(request, msg)
                return redirect(f'/blog/{pid}#form')
        else:
            msg = 'Your Comment did not submitted! did you fill all field correctly?'
            messages.error(request, msg)
            return redirect(f'/blog/{pid}#form')


    Form = CommentForm()
    post = Post.objects.get(Status = True, id = pid)
    comments = Comment.objects.filter(Post= post.id, Approved= True)

    Context = {'post': post, 'comments': comments, 'Form': Form}
    return render(request, 'blog/post.html', Context)

