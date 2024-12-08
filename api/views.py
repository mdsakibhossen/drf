from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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
        return JsonResponse({"error": "Students not found"}, status=404)


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
        return JsonResponse({"error": "Student not found"}, status=404)


# Create Student
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
