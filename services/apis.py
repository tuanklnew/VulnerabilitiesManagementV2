from services.models import ServiceModel
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import filters
from django.db.models import Q

from rest_framework.response import Response
from services.serializers import ServiceDetailSerializer, ServiceListSerializer, ServiceInputSerializer
from services.forms import ServiceAddForm
from django.contrib.auth.models import User
import uuid


class APIGetServiceDetail(RetrieveAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceDetailSerializer


class APIListServices(ListAPIView):
    serializer_class = ServiceListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'port')
    ordering_fields = ('name', 'port')

    def get_queryset(self):
        # check permission
        query = ServiceModel.objects.all()

        # filter by user who added service
        useradd = self.request.GET.get('useradd')
        if useradd:
            query = query.filter(createBy__username=useradd)

        # filter by user who latest updated service
        userupdate = self.request.GET.get('userupdate')
        if userupdate:
            query = query.filter(updateBy__username=userupdate)

        # filter by name of service
        name = self.request.GET.get('name')
        if name:
            query = query.filter(name=name)

        # filter by port
        port = self.request.GET.get('port')
        if port:
            query = query.filter(port=port)

        return query


class APICreateService(CreateAPIView):
    serializer_class = ServiceInputSerializer

    def perform_create(self, serializer):
        serializer.save(createBy=self.request.user, updateBy=self.request.user)


class APIUpdateService(RetrieveUpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceInputSerializer

    def perform_update(self, serializer):
        serializer.save(updateBy=self.request.user)


class APIDeleteService(RetrieveDestroyAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceInputSerializer
