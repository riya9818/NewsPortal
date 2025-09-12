from newspaper import views
from django.urls import path

urlpatterns =[
    path("",views.HomePageView.as_view(),name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
]