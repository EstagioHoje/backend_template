from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  
from django.http import HttpRequest
from django.views import View
from drf_yasg.utils import swagger_auto_schema
import uuid
from ..model.contract import Contract
from ..serializer.contract import ContractSerializer, CPFSerializer
from ..util.response import ResponseHandler
from ..serializer.contract import CPFSerializer, IDSerializer, UNISerializer, CNPJSerializer

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
        return ResponseHandler.GetSuccess(contracts_serializer.data)

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
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return ResponseHandler.GetSuccess(contracts_serializer.data)
    
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
        contracts_serializer=ContractSerializer(contracts,many=True)
        print(f'contract_serializer = {contracts_serializer.data}')
        return ResponseHandler.GetSuccess(contracts_serializer.data)

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
            return ResponseHandler.GetSuccess(contract_serializer.data)

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
            contract_data["id"] = uuid.uuid4()
            contract_serializer=ContractSerializer(data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PostSuccess(str(contract_data))
            return ResponseHandler.PostFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='PUT',
            request_body=ContractSerializer,
            operation_description="PUT /contract/post/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put(request):

        if request.method == 'PUT':
            contract_data = JSONParser().parse(request)
            cpf_contract = contract_data["cpf"]
            contract=Contract.objects.get(cpf=cpf_contract)
            contract_serializer=ContractSerializer(contract, data=contract_data)
            if contract_serializer.is_valid():
                contract_serializer.save()
                return ResponseHandler.PutSuccess(str(contract_data))
            return ResponseHandler.PutFailure((str(contract_serializer._errors)))
        
        return ResponseHandler._404Response()



    @swagger_auto_schema(
            method='DELETE',
            operation_description="DELETE /contract/delete/",
            query_serializer=CPFSerializer,
            tags=[TAG_NAME],
            )
    @api_view(['DELETE'])
    def delete(request):

        if request.method == 'DELETE':
            cpf_contract = request.GET["cpf"]
            contract=Contract.objects.get(cpf=cpf_contract)
            contract.delete()
            return ResponseHandler.DeleteSuccess(str(cpf_contract))
        
        return ResponseHandler._404Response()
