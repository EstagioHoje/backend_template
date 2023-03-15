from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from ..model.student import Student
from ..serializer.student import StudentSerializer
from bson.objectid import ObjectId
import uuid
from rest_framework.views import APIView

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views import View


# @method_decorator(name="teste")
TAG_NAME = "Student"
class StudentView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /student/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        students = Student.objects.all()
        students_serializer=StudentSerializer(students,many=True)
        print(f'student_serializer = {students_serializer.data}')
        return JsonResponse(students_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /student/get/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            cpf_student = request.GET["cpf"]
            student = Student.objects.filter(cpf=cpf_student)
            students_serializer=StudentSerializer(student,many=True)
            return JsonResponse(students_serializer.data,safe=False)

    @swagger_auto_schema(
            method='POST',
            request_body=StudentSerializer,
            operation_description="POST /student/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):

        if request.method == 'POST':
            student_data = JSONParser().parse(request)
            student_data["student_id"] = uuid.uuid1()
            student_serializer=StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return JsonResponse("Added Student Successfully \n\r"+str(student_data),safe=False)
            return JsonResponse("Failed to Add Student \n\r"+(str(student_serializer._errors)), safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='PUT',
            request_body=StudentSerializer,
            operation_description="PUT /student/post/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):

        if request.method == 'PUT':
            student_data = JSONParser().parse(request)
            cpf_student = student_data["cpf"]
            student=Student.objects.get(cpf=cpf_student)
            student_serializer=StudentSerializer(student, data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return JsonResponse("Added Student Successfully \n\r "+str(student_data),safe=False)
            return JsonResponse("Failed to Add Student \n\r"+str(student_data),safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /student/delete/",
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            cpf_student = request.GET["cpf"]
            student=Student.objects.get(cpf=cpf_student)
            student.delete()
            return JsonResponse("Delete Successfully \n\r"+str(cpf_student),safe=False)
        
        return JsonResponse("404",safe=False)
