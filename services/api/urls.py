from django.urls import path
from services.api import apis

app_name='services'

urlpatterns = [
    path('GetServiceDetail/<pk>', apis.APIGetServiceDetail.as_view(), name='GetDetail'),
    path('ListServices', apis.APIListServices.as_view(), name='List'),
    path('CreateService', apis.APICreateService.as_view(), name='Create'),
    path('UpdateService/<pk>', apis.APIUpdateService.as_view(), name='Update'),
    path('DeleteService/<pk>', apis.APIDeleteService.as_view(), name='Delete'),
    # path('AddService', apis.APIAddService.as_view(), name='APIAddService')
    ]
