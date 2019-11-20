from services.models import ServiceModel
# from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from services.api.pagination import ServiceListPagination
# from rest_framework.response import Response
from services.api.serializers import ServiceDetailSerializer, ServiceListSerializer, ServiceInputSerializer
# from django.contrib.auth.models import User
# import uuid


'''
API list services in detail information
'''

class APIGetServiceDetail(RetrieveAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceDetailSerializer


'''
API list services in general information: id, port, name,
'''

class APIListServices(ListAPIView):
    # Queryset for api
    queryset = ServiceModel.objects.all()

    # Serializer definition
    serializer_class = ServiceListSerializer

    # Filer backend for api
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)

    # Define search fields
    search_fields = ('name', 'port')

    # Define sort fields
    ordering_fields = '__all__'

    # Define default sort field
    ordering = ['name']

    # Define filter fields
    filter_fields = ['name', 'port']

    # Pagination class
    pagination_class = ServiceListPagination
    # def get_queryset(self):
    #     # check permission
    #     query = ServiceModel.objects.all()
    #
    #     # filter by user who added service
    #     useradd = self.request.GET.get('useradd')
    #     if useradd:
    #         query = query.filter(createBy__username=useradd)
    #
    #     # filter by user who latest updated service
    #     userupdate = self.request.GET.get('userupdate')
    #     if userupdate:
    #         query = query.filter(updateBy__username=userupdate)
    #
    #     # filter by name of service
    #     name = self.request.GET.get('name')
    #     if name:
    #         query = query.filter(name=name)
    #
    #     # filter by port
    #     port = self.request.GET.get('port')
    #     if port:
    #         query = query.filter(port=port)
    #
    #     return query


'''
API create service
'''

class APICreateService(CreateAPIView):
    serializer_class = ServiceInputSerializer

    def perform_create(self, serializer):
        serializer.save(createBy=self.request.user, updateBy=self.request.user)


'''
API update existing service
'''

class APIUpdateService(RetrieveUpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceInputSerializer

    def perform_update(self, serializer):
        serializer.save(updateBy=self.request.user)


'''
API delete existing service
'''

class APIDeleteService(RetrieveDestroyAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceInputSerializer
