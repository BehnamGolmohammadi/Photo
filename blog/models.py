from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    Author = models.ForeignKey(User, on_delete= models.CASCADE)
    Title = models.CharField(max_length= 255)
    Slug = models.SlugField(max_length= 255)
    Content = models.TextField()
    Image = models.ImageField(upload_to = user_directory_path)
    Status = models.BooleanField(default= False)
    # Tags = 
    # Category = 
    Created_Date = models.TimeField( default = timezone.now)
    Updated_Date = models.TimeField( default = timezone.now)
    Published_Date = models.TimeField()

    class META:
        pass


    def __str__(self):
        return self.Title