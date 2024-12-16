from django.urls import path
from .views import StudentAPI

urlpatterns = [
    # path("home/", view_name, name="name"),
    path("students/", StudentAPI.as_view(), name="students"),
    path("students/<int:pk>", StudentAPI.as_view(), name="student"),
]
