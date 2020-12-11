from django.urls import reverse
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category
    
    #def get_absolute_url(self):
     #   return reverse('mysite:mysite_topics',  
      #  args=[self.category
       # ])
class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, related_name="article")
    headline = models.CharField(max_length= 50)
    body =  models.TextField()
    published = models.DateTimeField(default=timezone.now)
    published_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name = "article")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.headline
class Question(models.Model):
    option_choices = (("A","blue"),("B","green"),("C","white"))
    question_field = models.CharField(max_length = 70)
    option = models.CharField(max_length=1,choices = option_choices)
    def __str__(self):
        return self.question_field