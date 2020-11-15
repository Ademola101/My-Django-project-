
from django.urls import path,include,re_path
from . import views
app_name="boards"
urlpatterns = [
    path("", views.BoardListView.as_view(), name = "home"),
    #path("",views.home, name="home"),
    path("<str:name>/",views.board_topics,name="board_topics"),
    path("<int:pk>/topics/<int:topic_pk>/",views.topic_posts,name= "topic_posts"),
    path("<int:pk>/new/",views.new_topic,name="new_topic"),
    path("<int:pk>/topics/<int:topic_pk>/reply", views.reply_topic, name="reply_topic"),
    path("<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/",views.PostUpdateView.as_view(), name = "edit_post"),
    path("new_subject",views.new_subject,name = "new_subject")
       #("sign_up/", views.Sign_up, name="Sign_up"),
   # path("logout/", views.logout_request, name = "logout"),
   # path("login/",
    # views.login, name = "login"),"""
    ] 