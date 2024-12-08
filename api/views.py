from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer


# Create your views here.
def students(request):
    try:
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.data, safe=False)
    except Student.DoesNotExist:
        # return HttpResponse(
        #     "Students not found", status=404, content_type="application/json"
        # )
        return JsonResponse("Students not found", safe=False)


def student(request, pk):
    try:
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.data)
    except Student.DoesNotExist:
        # return HttpResponse(
        #     "Student not found", status=404, content_type="application/json"
        # )
        return JsonResponse("Student not found", safe=False)
