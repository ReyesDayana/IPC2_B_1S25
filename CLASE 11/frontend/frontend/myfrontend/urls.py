from django.contrib import admin
from django.urls import path
from .views import index, admin_login, upload_xml, productos, ver_estadisticas


urlpatterns = [
    path('', index, name='index'),
    path('admin_login', admin_login, name='admin_login'),
    path('upload_xml', upload_xml, name='upload_xml'),
    path('producto', productos, name='productos'),
    path('ver_estadisticas', ver_estadisticas, name='ver_estadisticas' )

]