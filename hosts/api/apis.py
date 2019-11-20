from hosts.models import HostModel
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework import filters

from hosts.api.serializers import HostDetailSerializer, HostInputDataSerializer, HostListSerializer


class APIGetHostDetail(RetrieveAPIView):
    queryset = HostModel.objects.all()
    serializer_class = HostDetailSerializer


class APIListHosts(ListAPIView):
    serializer_class = HostListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('hostname', 'port')
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


class APICreateHost(CreateAPIView):
    serializer_class = HostInputDataSerializer

    def perform_create(self, serializer):
        serializer.save(createBy=self.request.user, updateBy=self.request.user)
#
#
# class APIUpdateService(RetrieveUpdateAPIView):
#     queryset = ServiceModel.objects.all()
#     serializer_class = ServiceInputDataSerializer
#
#     def perform_update(self, serializer):
#         serializer.save(updateBy=self.request.user)
#
#
# class APIDeleteService(RetrieveDestroyAPIView):
#     queryset = ServiceModel.objects.all()
#     serializer_class = ServiceInputDataSerializer
