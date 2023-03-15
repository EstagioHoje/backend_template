from django.http import HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from ..model.vacancy import Vacancy
from ..serializer.vacancy import VacancySerializer
import uuid

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.views import View


# @method_decorator(name="teste")
TAG_NAME = "Vacancy"
class VacancyView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /vacancy/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        vacancys = Vacancy.objects.all()
        vacancys_serializer=VacancySerializer(vacancys,many=True)
        print(f'vacancy_serializer = {vacancys_serializer.data}')
        return JsonResponse(vacancys_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /vacancy/get/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            id_vacancy = request.GET["id"]
            vacancy = Vacancy.objects.filter(id=id_vacancy)
            vacancys_serializer=VacancySerializer(vacancy,many=True)
            return JsonResponse(vacancys_serializer.data,safe=False)

    @swagger_auto_schema(
            method='POST',
            request_body=VacancySerializer,
            operation_description="POST /vacancy/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):
        
        if request.method == 'POST':
            vacancy_data = JSONParser().parse(request)
            vacancy_serializer=VacancySerializer(data=vacancy_data)
            if vacancy_serializer.is_valid():
                vacancy_serializer.save()
                return JsonResponse("Added Vacancy Successfully \n\r"+str(vacancy_data),safe=False)
            
            return JsonResponse("Failed to Add Vacancy \n\r"+(str(vacancy_serializer._errors)), safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='PUT',
            request_body=VacancySerializer,
            operation_description="PUT /vacancy/post/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):

        if request.method == 'PUT':
            vacancy_data = JSONParser().parse(request)
            id_vacancy = vacancy_data["id"]
            vacancy=Vacancy.objects.get(id=id_vacancy)
            vacancy_serializer=VacancySerializer(vacancy, data=vacancy_data)
            if vacancy_serializer.is_valid():
                vacancy_serializer.save()
                return JsonResponse("Added Successfully \n\r"+str(vacancy_data),safe=False)
            return JsonResponse("Failed to Add \n\r"+str(vacancy_data),safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /vacancy/delete/",
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            id_vacancy = request.GET["id"]
            vacancy=Vacancy.objects.get(id=id_vacancy)
            vacancy.delete()
            return JsonResponse("Delete Successfully \n\r"+str(id_vacancy),safe=False)
        
        return JsonResponse("404",safe=False)
