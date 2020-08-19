from django.contrib import admin
from .models import Category, Article
# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'published', 'created', 'updated')
