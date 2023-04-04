from django.http import HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from ..model.company import Company
from ..serializer.company import CompanySerializer, CNPJSerializer
import uuid

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.views import View


# @method_decorator(name="teste")
TAG_NAME = "Company"
class CompanyView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /company/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        companys = Company.objects.all()
        companys_serializer=CompanySerializer(companys,many=True)
        print(f'company_serializer = {companys_serializer.data}')
        return JsonResponse(companys_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /company/get/",
            query_serializer=CNPJSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            cnpj_company = request.GET["cnpj"]
            company = Company.objects.filter(cnpj=cnpj_company)
            companys_serializer=CompanySerializer(company,many=True)
            return JsonResponse(companys_serializer.data,safe=False)

    @swagger_auto_schema(
            method='POST',
            request_body=CompanySerializer,
            operation_description="POST /company/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):
        if request.method == 'POST':
            company_data = JSONParser().parse(request)
            company_data["company_id"] = uuid.uuid1()
            company_serializer=CompanySerializer(data=company_data)
            if company_serializer.is_valid():
                company_serializer.save()
                return JsonResponse("Added Company Successfully \n\r"+str(company_data),safe=False)
            
            return JsonResponse("Failed to Add Company \n\r"+(str(company_serializer._errors)), safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='PUT',
            request_body=CompanySerializer,
            operation_description="PUT /company/post/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):

        if request.method == 'PUT':
            company_data = JSONParser().parse(request)
            cnpj_company = company_data["cnpj"]
            company=Company.objects.get(cnpj=cnpj_company)
            company_serializer=CompanySerializer(company, data=company_data)
            if company_serializer.is_valid():
                company_serializer.save()
                return JsonResponse("Added Successfully \n\r"+str(company_data),safe=False)
            return JsonResponse("Failed to Add \n\r"+str(company_data),safe=False)
        
        return JsonResponse("404",safe=False)

    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /company/delete/",
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            cnpj_company = request.GET["cnpj"]
            company=Company.objects.get(cnpj=cnpj_company)
            company.delete()
            return JsonResponse("Delete Successfully \n\r"+str(cnpj_company),safe=False)
        
        return JsonResponse("404",safe=False)
