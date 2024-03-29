from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_info = openapi.Info(
    title="InternshipToday API",
    default_version='v1',
    description="InternshipTodayFirst Blog",
    terms_of_service="https://www.ourapp.com/policies/terms/",
    contact=openapi.Contact(email="vanderson.santos@usp.br"),
    license=openapi.License(name="MIT License"),
)
schema_view = get_schema_view(
    info=schema_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(r'student/', include('src.url.student')),
    path(r'company/', include('src.url.company')),
    path(r'vacancy/', include('src.url.vacancy')),
    path(r'teacher/', include('src.url.teacher')),
    path(r'contract/', include('src.url.contract')),
    path(r'report/', include('src.url.report')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]