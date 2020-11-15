#formsapi
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Topic,Post, Board
from django.contrib.auth.models import User
class NewTopicForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 
    'placeholder': 'What is on your mind?'}
), max_length=4000)
    class Meta:
        model = Topic
        #from the Topic model
        fields = ["subject","message"]
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput)
    class Meta:
        model = User
       #from the User model 
        fields = ('username', 'email', 'password1', 'password2')
class Postform(ModelForm):
    class Meta:
        model = Post
        fields = ("message",)
        labels = {"message":"Message"}
class NewSubjectform(ModelForm):
    class Meta:
        model = Board
        fields = "__all__"