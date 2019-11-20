from rest_framework import serializers
from hosts.models import HostModel, NetworkCard, OSModel


##########################################
#   NetworkCard Serializers
#

# Use for Nest Serializer of Host Objects
class NetworkCardSerializer(serializers.ModelSerializer):
    updateBy = serializers.CharField(source='updateBy.username')

    class Meta:
        model = NetworkCard
        exclude = ('host',)
        # fields = '__all__'


# Use for data input to create Host IP objects
class NetworkCardInputSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(many=False)

    class Meta:
        model = NetworkCard
        exclude = ('updateDate', 'updateBy')
        # fields = '__all__'


##########################################
#   OSModel Serializers
#

# Use for Nest Serializer of Host Objects
class OSSerializer(serializers.ModelSerializer):
    createBy = serializers.CharField(source='createBy.username')
    updateBy = serializers.CharField(source='updateBy.username')

    class Meta:
        model = OSModel
        fields = '__all__'


# Use for Nest Serializer of Host Objects
class OSInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = OSModel
        exclude = ('createBy', 'updateBy', 'createDate', 'updateDate')
        # fields = '__all__'


##########################################
#   HostModel Serializers
#
class HostDetailSerializer(serializers.ModelSerializer):
    createBy = serializers.CharField(source='createBy.username')
    updateBy = serializers.CharField(source='updateBy.username')
    ipAddr = NetworkCardSerializer(many=True, read_only=True)
    os = serializers.StringRelatedField(many=False)

    class Meta:
        model = HostModel
        exclude = ('services',)
        # fields = '__all__'


class HostListSerializer(serializers.ModelSerializer):
    ipAddrs = serializers.StringRelatedField(many=True)
    createBy = serializers.CharField(source='createBy.username')
    class Meta:
        model = HostModel
        fields = ('id', 'hostname', 'ipAddrs', 'createBy')


class HostInputDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = HostModel
        exclude = ('id', 'createBy', 'updateBy', 'createDate', 'updateDate')

