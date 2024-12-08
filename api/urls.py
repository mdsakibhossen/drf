from django.urls import path
from .views import students,student

urlpatterns = [
    # path("home/", view_name, name="name"),
    path("students/", students, name="students"),
    path("students/<int:pk>", student, name="student"),
]
