from django.db import models

# Create your models here.
class Contact(models.Model):
    First_Name = models.CharField(max_length= 255)
    Last_Name = models.CharField(max_length= 255)
    Email = models.EmailField(max_length= 255)
    Subject = models.CharField(max_length= 255)
    Message = models.TextField(max_length= 1200)
    Created_Date = models.DateTimeField(auto_now_add= True)
    Updated_Date = models.DateTimeField( auto_now = True)

    class META:
        ordering = ['-Created_Date']

    def __str__(self):
        return self.Email + ' : ' + self.Subject