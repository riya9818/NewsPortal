from django.urls import path,include

from report import views

app_name = "report"
urlpatterns = [
    path("users/", views.UserReportView.as_view(), name="users"),
    

]
