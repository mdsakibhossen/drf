from django.urls import path
from .views import students

urlpatterns = [
    # path("home/", view_name, name="name"),
    path("students/", students, name="students"),
    path("students/<int:pk>", students, name="student"),
]
