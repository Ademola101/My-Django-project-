from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .Forms import NewTopicForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render (request, "boards/home.html",{"boards": boards})
@login_required
def board_topics(request,pk):
  # boards = Board.objects.get(pk=pk)
   boards = get_object_or_404(Board,pk=pk)
   return render(request, "boards/topics.html",{"boards":boards}) 
def new_topic(request,pk):
    boards = get_object_or_404(Board,pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.boards = boards
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user)
            return redirect('board_topics', pk=boards.pk)  
            # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'boards': boards, 'form': form})

"""def Sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login (request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = SignUpForm
    return render(request, "boards/Sign_up.html",{"form":form})
def logout_request (request):
    logout(request)
    return redirect ("home")
def login(request):
    form = AuthenticationForm()
    return render(request, "boards/login.html",{ "form":form})"""