from newspaper import views
from django.urls import path

urlpatterns =[
    path("",views.HomePageView.as_view(),name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("about/",views.AboutView.as_view(), name="about")
]