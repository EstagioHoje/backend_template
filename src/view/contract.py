from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  
from django.http import HttpRequest, JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
import uuid
from ..model.contract import Contract
from ..model.report import Report
from ..serializer.contract import ContractSerializer, CPFSerializer
from ..util.response import ResponseHandler
from ..serializer.contract import CPFSerializer, IDSerializer, UNISerializer, CNPJSerializer, REJECTSerializer
from ..serializer.report import ReportSerializer
from ..model.student import Student
from ..serializer.student import StudentSerializer
from ..model.company import Company
from ..serializer.company import CompanySerializer
import json 
from collections import OrderedDict

TAG_NAME = "Contract"
class ContractView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all_cpf/",
            tags=[TAG_NAME],
            query_serializer=CPFSerializer,
            )
    @api_view(['GET'])
    def get_all_cpf(request: HttpRequest):
        cpf = request.GET["cpf"]
        contracts = Contract.objects.filter(student_cpf=cpf)
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return JsonResponse(contracts_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all_cnpj/",
            tags=[TAG_NAME],
            query_serializer=CNPJSerializer,
            )
    @api_view(['GET'])
    def get_all_cnpj(request: HttpRequest):
        cnpj = request.GET["cnpj"]
        contracts = Contract.objects.filter(company_cnpj=cnpj)
        contracts = contracts.exclude(status="a")
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return JsonResponse(contracts_serializer.data,safe=False)
    
    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all_uni/",
            tags=[TAG_NAME],
            query_serializer=UNISerializer,
            )
    @api_view(['GET'])
    def get_all_uni(request: HttpRequest):
        uni = request.GET["uni"]
        contracts = Contract.objects.filter(student_college=uni)
        contracts = contracts.exclude(status="a")
        contracts = contracts.exclude(status="f")
        contracts = contracts.exclude(status="x")
        contracts = contracts.exclude(status="y")
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return JsonResponse(contracts_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        contracts = Contract.objects.all()
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return ResponseHandler.GetSuccess(contracts_serializer.data)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get/",
            query_serializer=IDSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_one(request: HttpRequest):
        if request.method == 'GET':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            return JsonResponse(contract_serializer.data,safe=True)





    @swagger_auto_schema(
            method='PUT',
            request_body=ContractSerializer,
            operation_description="PUT /contract/put/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):
        
        if request.method == 'PUT':
            print("teste")
            contract_data = JSONParser().parse(request)
            id = uuid.UUID(contract_data["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/sign_student/",
            tags=[TAG_NAME],
            query_serializer=IDSerializer,
            )
    @api_view(['PUT'])
    def sign_student(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "x"
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save(update_fields=['status'])
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/sign_company/",
            tags=[TAG_NAME],
            query_serializer=IDSerializer,
            )
    @api_view(['PUT'])
    def sign_company(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "b"
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save(update_fields=['status'])
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/sign_teacher/",
            tags=[TAG_NAME],
            query_serializer=IDSerializer,
            )
    @api_view(['PUT'])
    def sign_teacher(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "c"
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                print(contract_data)
                print(type(contract_data))
                report_data = {
                    "student_cpf": contract_data["student_cpf"],
                    "student_college": contract_data["student_college"],
                    "company_cnpj": contract_data["student_college"],
                    "contract_data": contract_data
                }
                report_serializer = ReportSerializer(data=report_data)
                if(report_serializer.is_valid()):
                    report_serializer.save()
                    contract_serializer.save()
                    return ResponseHandler.PutSuccess(str(contract_data))
                return ResponseHandler.PutFailure((str(report_serializer._errors)))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/reject_student/",
            tags=[TAG_NAME],
            query_serializer=REJECTSerializer,
            )
    @api_view(['PUT'])
    def reject_student(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "f"
            contract_data["reject_reason"] = request.GET["reject_reason"]
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/reject_company/",
            tags=[TAG_NAME],
            query_serializer=REJECTSerializer,
            )
    @api_view(['PUT'])
    def reject_company(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "y"
            contract_data["reject_reason"] = request.GET["reject_reason"]
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='PUT',
            operation_description="PUT /contract/reject_teacher/",
            tags=[TAG_NAME],
            query_serializer=REJECTSerializer,
            )
    @api_view(['PUT'])
    def reject_teacher(request):

        if request.method == 'PUT':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract_serializer=ContractSerializer(contract)
            contract_data = contract_serializer.data
            contract_data["status"] = "g"
            contract_data["reject_reason"] = request.GET["reject_reason"]
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()



    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /contract/delete/",
            query_serializer=IDSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            id = uuid.UUID(request.GET["id"])
            contract = Contract.objects.get(id=id)
            contract.delete()
            return ResponseHandler.DeleteSuccess(str(id))
        
        return ResponseHandler._404Response()
    
    @swagger_auto_schema(
            method='POST',
            request_body=ContractSerializer,
            operation_description="POST /contract/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):

        if request.method == 'POST':
            contract_data = JSONParser().parse(request)
            cpf_student=contract_data["student_cpf"]
            cnpj_company=contract_data["company_cnpj"]

            student = Student.objects.filter(cpf=cpf_student)
            students_serializer=StudentSerializer(student,many=True)

            company = Company.objects.filter(cnpj=cnpj_company)
            companys_serializer=CompanySerializer(company,many=True)
           
            dict_student = dict(students_serializer.data[0])
            dict_company = dict(companys_serializer.data[0])



            contract_data["student_data"] = dict_student
            contract_data["company_data"] = dict_company
            contract_data["student_college"] = dict_student["college"]
            contract_serializer=ContractSerializer(data=contract_data)
            print(dict_student["college"])
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PostSuccess(str(contract_data))
            return ResponseHandler.PostFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()
