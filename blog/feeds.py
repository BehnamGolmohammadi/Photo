from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class LatestPostsFeed(Feed):
    title = 'Photo blog posts'
    link = 'rss/'
    description = 'Here you can see a lot of experience of our team and customers.'

    def items(self):
        return Post.objects.filter(Status = True)[:10]

    def item_title(self, item):
        return item.Title

    def item_description(self, item):
        return ' '.join((item.Content).split()[:35])

    def item_link(self, item):
        return reverse(viewname= 'blog:post', kwargs = {'pid' : item.id})