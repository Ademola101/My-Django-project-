
from django.urls import path,include,re_path
from . import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:pk>/",views.board_topics,name="board_topics"),
    path("<int:pk>/new/",views.new_topic,name="new_topic"),
   #("sign_up/", views.Sign_up, name="Sign_up"),
   # path("logout/", views.logout_request, name = "logout"),
   # path("login/",
    # views.login, name = "login"),"""
    ] 