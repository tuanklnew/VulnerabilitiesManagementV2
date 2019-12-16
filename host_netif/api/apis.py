from services.models import ServiceModel
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from core.pagination import ListPagination
from services.api.serializers import ServiceDetailSerializer, ServiceListSerializer, ServiceInputSerializer


'''
API get service in detail information
'''

class APIGetServiceDetail(RetrieveAPIView):
    queryset = ServiceModel.objects.filter(isDelete=False)
    serializer_class = ServiceDetailSerializer


'''
API list services in general information: id, port, name,
'''

class APIListServices(ListAPIView):
    # Queryset for api
    queryset = ServiceModel.objects.filter(isDelete=False)

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
    pagination_class = ListPagination


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
    queryset = ServiceModel.objects.filter(isDelete=False)
    serializer_class = ServiceInputSerializer

    def perform_update(self, serializer):
        serializer.save(updateBy=self.request.user)


'''
API delete existing service
'''

class APIDeleteService(RetrieveDestroyAPIView):
    queryset = ServiceModel.objects.filter(isDelete=False)
    serializer_class = ServiceInputSerializer

    def perform_destroy(self, instance):
        instance.isDelete = True
        instance.save()
