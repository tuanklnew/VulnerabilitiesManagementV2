from django.urls import path
from hosts.api import apis

app_name='hosts'

urlpatterns = [
    path('GetHostDetail/<pk>', apis.APIGetHostDetail.as_view(), name='GetDetail'),
    # path('ListServices', apis.APIListServices.as_view(), name='List'),
    path('CreateHost', apis.APICreateHost.as_view(), name='Create'),
    # path('UpdateService/<pk>', apis.APIUpdateService.as_view(), name='Update'),
    # path('DeleteService/<pk>', apis.APIDeleteService.as_view(), name='Delete'),
    ]
