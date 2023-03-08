from django.contrib import admin
from django.urls import path, include, re_path
from src.main import hello_world
from django.conf.urls import url
# from rest_framework_swagger.     import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_info = openapi.Info(
    title="Swagger First Blog ",
    default_version='v1',
    description="Test Swagger First Blog",
    terms_of_service="https://www.ourapp.com/policies/terms/",
    contact=openapi.Contact(email="contact@swaggerBlog.local"),
    license=openapi.License(name="Test License"),
)
schema_view = get_schema_view(
    info=schema_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('openapi', schema_view, name='openapi-schema'),
    path(r'', hello_world),
    path(r'task/', include('src.url.task')),
    path(r'student/', include('src.url.student')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]