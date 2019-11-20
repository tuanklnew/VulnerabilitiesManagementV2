from rest_framework import serializers
from services.models import ServiceModel


class ServiceDetailSerializer(serializers.ModelSerializer):
    createBy = serializers.CharField(source='createBy.username')
    updateBy = serializers.CharField(source='updateBy.username')

    class Meta:
        model = ServiceModel
        # exclude = ('createBy', 'updateBy')
        fields = '__all__'

        extra_kwargs = {
            'createBy': {'read_only': True},
            'updateBy': {'read_only': True},
            'dateCreated': {'read_only': True},
            'dateUpdate': {'read_only': True},
        }


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'port')


class ServiceInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceModel
        fields = ('name', 'port', 'description')

