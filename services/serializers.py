from rest_framework import serializers
from services.models import ServiceModel


class ServiceDetailSerializer(serializers.ModelSerializer):
    createBy = serializers.CharField(source='createBy.username')
    updateBy = serializers.CharField(source='updateBy.username')

    class Meta:
        model = ServiceModel
        # exclude = ('createBy', 'updateBy')
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'port')


class ServiceInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceModel
        fields = ('name', 'port', 'description')

