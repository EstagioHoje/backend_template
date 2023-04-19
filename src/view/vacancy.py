from django.http import HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from ..model.vacancy import Vacancy
from ..serializer.vacancy import VacancySerializer
from ..serializer.student import StudentSerializer
import uuid
from ..model.student import Student
from ..serializer.vacancy import ApplySerializer, SearchID, SearchCNPJ

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
            operation_description="GET /vacancy/get/all_cnpj/",
            query_serializer=SearchCNPJ,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all_cnpj(request: HttpRequest):
        cnpj_vacancy = request.GET["cnpj"]
        vacancys = Vacancy.objects.filter(company_cnpj=cnpj_vacancy)
        vacancys_serializer=VacancySerializer(vacancys,many=True)
        print(f'vacancy_serializer = {vacancys_serializer.data}')
        return JsonResponse(vacancys_serializer.data,safe=False)   
    
    @swagger_auto_schema(
            method='GET',
            operation_description="GET /vacancy/getCandidates/",
            query_serializer=SearchID,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_candidates(request: HttpRequest):
        if request.method == 'GET':
            id_vacancy = uuid.UUID(request.GET["id"])
            vacancy = Vacancy.objects.get(id=id_vacancy)
            vacancy_serializer=VacancySerializer(vacancy)
            cpfs = vacancy_serializer.data["candidates"]["cpfs"]
            students = Student.objects.filter(cpf__in=cpfs)
            students_serializer = StudentSerializer(students, many=True)
            return JsonResponse(students_serializer.data,safe=False)
        return JsonResponse("404",safe=False)



    @swagger_auto_schema(
            method='GET',
            operation_description="GET /vacancy/getID/",
            query_serializer=SearchID,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one_id(request: HttpRequest):
        if request.method == 'GET':
            print("teste")
            id_vacancy = uuid.UUID(request.GET["id"])
            vacancy = Vacancy.objects.filter(id=id_vacancy)
            vacancys_serializer=VacancySerializer(vacancy,many=True)
            return JsonResponse(vacancys_serializer.data,safe=False)
        return JsonResponse("404",safe=False)
    


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
            id_vacancy = uuid.UUID(vacancy_data["id"])
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
            query_serializer=SearchID,
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            id_vacancy = uuid.UUID(request.GET["id"])
            vacancy=Vacancy.objects.get(id=id_vacancy)
            vacancy.delete()
            return JsonResponse("Delete Successfully \n\r"+str(id_vacancy),safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /vacancy/apply/",
            tags=[TAG_NAME],
            query_serializer=ApplySerializer,
            )
    @api_view(['PUT'])
    def apply(request):
        if request.method == 'PUT':
            id_vacancy = request.GET["id_vacancy"]
            cpf_student = request.GET["cpf"]

            vacancy = Vacancy.objects.get(id=uuid.UUID(id_vacancy)) #uuid4
            vacancy_serializer = VacancySerializer(vacancy)
            is_to_add_cpf = True

            if not("cpfs" in vacancy_serializer.data["candidates"]):
                vacancy_serializer.data["candidates"]["cpfs"] = []
            else:
                if cpf_student in vacancy_serializer.data["candidates"]["cpfs"]:
                    is_to_add_cpf = False

            if is_to_add_cpf:
                vacancy_serializer.data["candidates"]["cpfs"].append(cpf_student)

                vacancy_serializer = VacancySerializer(vacancy,data=vacancy_serializer.data)

                if vacancy_serializer.is_valid():
                    vacancy_serializer.save()
                    return JsonResponse("Added Successfully \n\r"+str(cpf_student),safe=False)
                return JsonResponse("Failed to Add \n\r"+str(cpf_student),safe=False)
            else:
                return JsonResponse(f"Failed to Add \n\r cpf : {str(cpf_student)} already add",safe=False)
        
        return JsonResponse("404",safe=False)