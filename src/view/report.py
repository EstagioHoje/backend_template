from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  

from django.http import HttpRequest, JsonResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
import uuid
from ..model.report import Report
from ..serializer.report import ReportSerializer
from ..serializer.report import CPFSerializer, IDSerializer, UNISerializer, CNPJSerializer
from ..util.response import ResponseHandler

TAG_NAME = "Report"
class ReportView(View):

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /report/get_all_cpf/",
            tags=[TAG_NAME],
            query_serializer=CPFSerializer,
            )
    @api_view(['GET'])
    def get_all_cpf(request: HttpRequest):
        cpf = request.GET["cpf"]
        reports = Report.objects.filter(student_cpf=cpf)
        reports_serializer=ReportSerializer(reports,many=True)
        print(f'contract_serializer = {reports_serializer.data}')
        return JsonResponse(reports_serializer.data,safe=False)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /report/get_all_cnpj/",
            tags=[TAG_NAME],
            query_serializer=CNPJSerializer,
            )
    @api_view(['GET'])
    def get_all_cnpj(request: HttpRequest):
        cnpj = request.GET["cnpj"]
        reports = Report.objects.filter(company_cnpj=cnpj)
        reports_serializer=ReportSerializer(reports,many=True)
        print(f'contract_serializer = {reports_serializer.data}')
        return ResponseHandler.GetSuccess(reports_serializer.data)
    
    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all_uni/",
            tags=[TAG_NAME],
            query_serializer=UNISerializer,
            )
    @api_view(['GET'])
    def get_all_uni(request: HttpRequest):
        uni = request.GET["uni"]
        reports = Report.objects.filter(student_college=uni)
        reports_serializer=ReportSerializer(reports,many=True)
        print(f'contract_serializer = {reports_serializer.data}')
        return ResponseHandler.GetSuccess(reports_serializer.data)

    @swagger_auto_schema(
            method='GET',
            operation_description="GET /contract/get_all/",
            tags=[TAG_NAME],
            )
    @api_view(['GET'])
    def get_all(request: HttpRequest):
        reports = Report.objects.all()
        reports_serializer=ReportSerializer(reports,many=True)
        print(f'contract_serializer = {reports_serializer.data}')
        return ResponseHandler.GetSuccess(reports_serializer.data)

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
            contract = Report.objects.get(id=id)
            report_serializer=ReportSerializer(contract)
            return ResponseHandler.GetSuccess(report_serializer.data)


    @swagger_auto_schema(
            method='POST',
            request_body=ReportSerializer,
            operation_description="POST /report/post/",
            tags=[TAG_NAME],
            )
    @api_view(['POST'])
    def post(request):
        if request.method == 'POST':
            report_data = JSONParser().parse(request)
            report_serializer = ReportSerializer(data=report_data)
            if report_serializer.is_valid():
                report_serializer.save()
                return ResponseHandler.PostSuccess(str(report_data))
            return ResponseHandler.PostFailure((str(report_serializer._errors)))
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='PUT',
            request_body=ReportSerializer,
            operation_description="PUT /report/put/student/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put_student(request):
        if request.method == 'PUT':
            report_data = JSONParser().parse(request)
            id_report = report_data["id"]
            report = Report.objects.get(id= id_report)
            report_serializer = ReportSerializer(report, data= report_data)
            if report_serializer.is_valid():
                report_serializer.save(update_fields=['student_report'])
                return ResponseHandler.PutSuccess(str(report_data))
            return ResponseHandler.PutFailure((str(report_serializer._errors)))
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='PUT',
            request_body=ReportSerializer,
            operation_description="PUT /report/put/company/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put_company(request):
        if request.method == 'PUT':
            report_data = JSONParser().parse(request)
            id_report = report_data["id"]
            report = Report.objects.get(id= id_report)
            report_serializer = ReportSerializer(report, data= report_data)
            if report_serializer.is_valid():
                report_serializer.save(update_fields=['company_report'])
                return ResponseHandler.PutSuccess(str(report_data))
            return ResponseHandler.PutFailure((str(report_serializer._errors)))
        return ResponseHandler._404Response()

    @swagger_auto_schema(
            method='PUT',
            request_body=ReportSerializer,
            operation_description="PUT /report/put/teacher/",
            tags=[TAG_NAME],
            )
    @api_view(['PUT'])
    def put_teacher(request):
        if request.method == 'PUT':
            report_data = JSONParser().parse(request)
            id_report = report_data["id"]
            report = Report.objects.get(id= id_report)
            report_serializer = ReportSerializer(report, data= report_data)
            if report_serializer.is_valid():
                report_serializer.save(update_fields=['grade'])
                return ResponseHandler.PutSuccess(str(report_data))
            return ResponseHandler.PutFailure((str(report_serializer._errors)))
        return ResponseHandler._404Response()
