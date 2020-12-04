
from django.urls import path,include,re_path
from . import views
from boards.views import BoardListView
urlpatterns = [
    path("", BoardListView.as_view(), name = "home"),
    #path("",views.home, name="home"),
    path("<str:name>/",views.board_topics,name="board_topics"),
    path("<str:name>/topics/<str:topic_subject>/",views.topic_posts,name= "topic_posts"),
    path("<str:name>/new/",views.new_topic,name="new_topic"),
    path("<str:name>/topics/<str:topic_name>/reply", views.reply_topic, name="reply_topic"),
    path("<str:name>/topics/<str:topic_name>/posts/<str:post_name>/edit/",views.PostUpdateView.as_view(), name = "edit_post"),
    path("new_subject",views.new_subject,name = "new_subject")
       #("sign_up/", views.Sign_up, name="Sign_up"),
   # path("logout/", views.logout_request, name = "logout"),
   # path("login/",
    # views.login, name = "login"),"""
    ] 