from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='files/user_avatar', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='files/blog_img')
    content = RichTextField()
    create_time: models.DateTimeField(editable=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    auther = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
