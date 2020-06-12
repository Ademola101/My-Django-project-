#account url
from django.urls import path,include,re_path
from accounts import views as accounts_views
from  django.contrib import admin
from django.contrib.auth import views
urlpatterns =[
    path("accounts/sign_up/",
  accounts_views.sign_up, 
    name = "sign-up"),
]
