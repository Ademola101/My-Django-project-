from django.shortcuts import render, get_object_or_404,redirect,get_list_or_404
from django.http import HttpResponse
from django.db.models import Count
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .Forms import NewTopicForm, SignUpForm,Postform,NewSubjectform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
# Create your views here.

class BoardListView(ListView):
    model = Board
    context_object_name =  "boards"
    template_name = "boards/home.html"
#def home(request):
 #   boards = Board.objects.all()
  #  return render (request, "boards/home.html",{"boards": boards})
@login_required
def board_topics(request,name):
   boards = Board.objects.get(name=name)
   #boards = get_object_or_404(Board,name=name)
   #name for url matching, to have differnrt board in topics.html2
   topics = boards.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
   return render(request, "boards/topics.html",{"boards":boards,"topics":topics}) 
def new_topic(request,name):
    boards = get_object_or_404(Board,name=name)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():# if request is POST and from is valid
            #create the topic form from the Topic model
            topic = form.save(commit=False)
            #set the parameter that are not defined
            #  in the form.py field but are in Topic model
            topic.boards = boards
            topic.starter = request.user
            topic.save()
            Post.objects.create(
               message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user)

        return redirect('topic_posts', name=name,topic_subject=topic.subject)  
            # TODO: redirect to the created topic page 
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'boards': boards, 'form': form})
#class NewTopicVeiw(FormView):
 #   template_name = 'boards/new_topic.html'
  #  form_class = NewTopicForm
   # success_url = "/thanks/"
    #def form_valid(self,form):
     #   pass


         
def topic_posts(request,name,topic_subject):
    topic = get_object_or_404(Topic,boards__name=name, subject= topic_subject) 
    topic.views += 1
    topic.save()
    context = {"topic":topic}
    return render(request,"boards/topic_posts.html",context)
@login_required
def reply_topic(request, name, topic_subject):
    topic = get_object_or_404(Topic, boards__name=name, subject=topic_subject)
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', name=name, topic_subject=topic_subject)
    else:
        form = Postform()
    return render(request, 'boards/reply_post.html', {'topic': topic, 'form': form})
def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ["message"]
    template_name = "boards/edit_post.html"
    pk_url_kwarg = "post_pk"
    context_object_name = "post" 
    success_url = "/thanks/"
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', name=post.topic.boards.name, topic_subject=post.topic.subject)
        
def new_subject(request):
    if request.method == "POST":
        form = NewSubjectform(request.POST)
        if form.is_valid():
            Board.objects.create(
                name = form.cleaned_data.get("name"),
                description = form.cleaned_data.get("description"))
            return redirect("home")
    else:
        form = NewSubjectform()
    return render(request,"boards/new_subject.html",{"form":form})

    