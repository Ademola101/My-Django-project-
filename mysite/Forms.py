from mysite.models import Article,Question
from django.contrib.auth.models import User
from django import forms
class Mysite_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["headline","body"]
class Question_form(forms.ModelForm):
    class Meta:
        model= Question
        fields = "__all__"
