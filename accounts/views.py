
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .Forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
# Create your views here.

def sign_up(request):
    form_class = SignUpForm
    form = form_class(request.POST or None)
    if request.method == "POST":

        if  form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login (request, user)
            return redirect("home")                  
        else:
             form = form_class()
    return render(request, "registration/Sign_up.html",{"form":form})
@method_decorator(login_required,name = "dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ["username","first_name","last_name"]
    template_name = "accounts/my_account.html"
    success_url = reverse_lazy("home")
    def get_object(self):
        return self.request.user