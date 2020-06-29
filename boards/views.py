from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .Forms import NewTopicForm, SignUpForm,Postform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render (request, "boards/home.html",{"boards": boards})
@login_required
def board_topics(request,pk):
  # boards = Board.objects.get(pk=pk)
   boards = get_object_or_404(Board,pk=pk)
   topics = boards.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
   return render(request, "boards/topics.html",{"boards":boards,"topics":topics}) 
def new_topic(request,pk):
    boards = get_object_or_404(Board,pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():# if request is POST and from is valid
            topic = form.save(commit=False)
            topic.boards = boards
            topic.starter = request.user
            topic.save()
            Post.objects.create(
               message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user)
            return redirect('topic_posts', pk=pk,topic_pk=topic.pk)  
            # TODO: redirect to the created topic page 
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'boards': boards, 'form': form})

def topic_posts(request,pk,topic_pk):
    topic = get_object_or_404(Topic,boards__pk=pk,pk=topic_pk) 
    topic.views += 1
    topic.save()
    context = {"topic":topic}
    return render(request,"boards/topic_posts.html",context)
@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, boards__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = Postform()
    return render(request, 'boards/reply_post.html', {'topic': topic, 'form': form})
class PostUpdateView(UpdateView):
    model = Post
    fields = ("message",)
    template_name = "boards/edit_post.html"
    pk_url_kwarg = "post_pk"
    context_object_name = "post"
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.boards.pk, topic_pk=post.topic.pk)
        
