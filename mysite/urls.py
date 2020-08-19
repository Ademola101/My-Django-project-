#mysite/url
from django.urls import path
from . import views
app_name = "mysite"
urlpatterns = [
    path("", views.MysiteListView.as_view(), name = "mysite_home"),
    path("<int:pk>/",views.mysite_topics, name="mysite_topics")
]
