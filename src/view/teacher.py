from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  
from django.http import HttpRequest
from django.views import View
from drf_yasg.utils import swagger_auto_schema
import uuid
from ..model.teacher import Teacher
from ..serializer.teacher import TeacherSerializer, CPFSerializer
from ..util.response import ResponseHandler

TAG_NAME = "Teacher"
class TeacherView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /teacher/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        teachers = Teacher.objects.all()
        teachers_serializer=TeacherSerializer(teachers,many=True)
        print(f'teacher_serializer = {teachers_serializer.data}')
        return ResponseHandler.GetSuccess(teachers_serializer.data)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /teacher/get/",
            query_serializer=CPFSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            cpf_teacher = request.GET["cpf"]
            teacher = Teacher.objects.filter(cpf=cpf_teacher)
            teachers_serializer=TeacherSerializer(teacher,many=True)
            return ResponseHandler.GetSuccess(teachers_serializer.data)

    @swagger_auto_schema(
            method='POST',
            request_body=TeacherSerializer,
            operation_description="POST /teacher/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):

        if request.method == 'POST':
            teacher_data = JSONParser().parse(request)
            teacher_data["id"] = uuid.uuid4()
            teacher_serializer=TeacherSerializer(data=teacher_data)
            if teacher_serializer.is_valid():
                teacher_serializer.save()
                return ResponseHandler.PostSuccess(str(teacher_data))
            return ResponseHandler.PostFailure((str(teacher_serializer._errors)))
        
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='PUT',
            request_body=TeacherSerializer,
            operation_description="PUT /teacher/post/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):

        if request.method == 'PUT':
            teacher_data = JSONParser().parse(request)
            cpf_teacher = teacher_data["cpf"]
            teacher=Teacher.objects.get(cpf=cpf_teacher)
            teacher_serializer=TeacherSerializer(teacher, data=teacher_data)
            if teacher_serializer.is_valid():
                teacher_serializer.save()
                return ResponseHandler.PutSuccess(str(teacher_data))
            return ResponseHandler.PutFailure((str(teacher_serializer._errors)))
        
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /teacher/delete/",
            query_serializer=CPFSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            cpf_teacher = request.GET["cpf"]
            teacher=Teacher.objects.get(cpf=cpf_teacher)
            teacher.delete()
            return ResponseHandler.DeleteSuccess(str(cpf_teacher))
        
        return ResponseHandler._404Response()
