from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    Author = models.ForeignKey(User, on_delete= models.CASCADE)
    Title = models.CharField(max_length= 255)
    Slug = models.SlugField(max_length= 255)
    Content = models.TextField()
    Image = models.ImageField(upload_to = 'blog/', default = 'blog/Default.png')
    Status = models.BooleanField(default= False)
    # Tags = 
    # Category = 
    Created_Date = models.DateTimeField( auto_now_add= True)
    Updated_Date = models.DateTimeField( auto_now= True)
    Published_Date = models.DateTimeField(null= True)

    class META:
        pass


    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
        args= [self.Published_Date,
        self.Slug,
        self.id]
        )