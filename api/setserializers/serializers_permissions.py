from rest_framework import serializers
from api.models.permissions import Permissions


class PermissionsSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = Permissions
        fields = ['permissions_name', 'permissions_created', 'permission_status_check']