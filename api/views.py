from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def students(request, pk=None):
    if request.method == "GET":
        try:
            if pk == None:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                stu = Student.objects.get(id=pk)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student Not Found"}, status=404)

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Student created successfully!"}, status=200
            )
        return JsonResponse(serializer.errors)

    if request.method == "PATCH":
        stu = Student.objects.get(id=pk)
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        # Use partial=True to allow partial updates
        serializer = StudentSerializer(instance=stu, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Student updated successfully!"}, status=200
            )
        return JsonResponse(serializer.errors, status=400)

    if request.method == "PUT":
        stu = Student.objects.get(id=pk)
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        # Pass both the instance and new data to the serializer
        serializer = StudentSerializer(instance=stu, data=python_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Student updated successfully!"}, status=200
            )
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return JsonResponse({"message": "Student deleted successfully"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student Not Found"}, status=404)
