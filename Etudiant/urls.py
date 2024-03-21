from django.urls import path
from Etudiant import views
urlpatterns = [
    path('',views.add_show, name = "addandshow"),
    path('/delete/<int:id>/',views.delete_data, name = "deletedata"),
]