from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import UpdateView, ListView
from mysite.models import Category, Article
from django.contrib.auth.models import User
from mysite.Forms import Mysite_form
# Create your views here.
class MysiteListView(ListView):
    model = Category
    context_object_name =  "categorys"
    template_name = "mysite/home.html"
def mysite_topics(request,pk):
    #article = get_object_or_404(Article, pk=pk)
    article = Article.objects.all()
    categorys = get_object_or_404(Category,pk=pk) 
    return render(request,"mysite/topics.html", {"categorys":categorys,"article":article})
def new_post(request,pk):
    categorys = get_object_or_404(Category,pk=pk)
    user = User.objects.first()
    if request.method == "POST":
        form = Mysite_form(request.Post)
        if form.is_valid():
            article = form.save(commit=False)
            article.categorys = categorys
            article.published_by = request.user
            article.save()
            return redirect("mysite_topics", pk = pk)
    else:
        form = Mysite_form()
    return render(request, "mysite/topic.html",{"categorys":categorys, "form":form})
    