from django.contrib import admin
from .models import Category, Article,Question
# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Question)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'published', 'created', 'updated')
