from django.db import models
from course.models import Teacher
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blog(models.Model):
    title = models.CharField(max_length=25)
    post = models.TextField()
    image = models.ImageField(upload_to='blogs/blogs/')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


