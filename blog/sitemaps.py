from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from blog.models import Post

class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(Status = True)

    def lastmod(self, obj):
        return obj.Published_Date

    def location(self, item):
        return reverse(viewname = 'blog:post', kwargs = {'pid': item.id})
