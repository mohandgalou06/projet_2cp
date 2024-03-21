from django.urls import path
from student import views
urlpatterns = [
    path('',views.add_show, name = "addandshow"),
]

