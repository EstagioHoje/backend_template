from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  
from django.http import HttpRequest
from django.views import View
from drf_yasg.utils import swagger_auto_schema
import uuid
from ..model.student import Student
from ..serializer.student import StudentSerializer, CPFSerializer, COMPANYSerializer
from ..util.response import ResponseHandler

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
        return ResponseHandler.GetSuccess(students_serializer.data)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /student/get/",
            query_serializer=CPFSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            cpf_student = request.GET["cpf"]
            student = Student.objects.filter(cpf=cpf_student)
            students_serializer=StudentSerializer(student,many=True)
            return ResponseHandler.GetSuccess(students_serializer.data)
        
    @swagger_auto_schema(
            method='GET',
            operation_description="GET /student/get_company/",
            query_serializer=COMPANYSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_company(request: HttpRequest):
        if request.method == 'GET':
            id = uuid.UUID(request.GET["id"])
            cpf_student = request.GET["cpf"]
            student = Student.objects.filter(cpf=cpf_student,id=id)
            students_serializer=StudentSerializer(student,many=True)
            return ResponseHandler.GetSuccess(students_serializer.data)

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
            student_data["id"] = uuid.uuid4()
            student_serializer=StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return ResponseHandler.PostSuccess(str(student_data))
            return ResponseHandler.PostFailure((str(student_serializer._errors)))
        
        return ResponseHandler._404Response()

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
                return ResponseHandler.PutSuccess(str(student_data))
            return ResponseHandler.PutFailure((str(student_serializer._errors)))
        
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /student/delete/",
            query_serializer=CPFSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            cpf_student = request.GET["cpf"]
            student=Student.objects.get(cpf=cpf_student)
            student.delete()
            return ResponseHandler.DeleteSuccess(str(cpf_student))
        
        return ResponseHandler._404Response()
