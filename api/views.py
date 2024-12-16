from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        # print("Args", args)
        # print("KWArgs", kwargs)
        pk = kwargs.get("pk")
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

    def post(self, request, *args, **kwargs):
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

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
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

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
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

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return JsonResponse({"message": "Student deleted successfully"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student Not Found"}, status=404)
