from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    image = models.ImageField(upload_to='post')
    description = models.TextField()
    name = models.TextField(null=True)


class Profile(models.Model):   
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True) 
    phone=models.CharField(max_length=200)
    bio=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='profilepic')  

    def __str__(self):
            return str(self.user)   

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    comment= models.TextField()
    post= models.ForeignKey(Post,on_delete=models.CASCADE,null=True)               
