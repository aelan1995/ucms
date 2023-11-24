from rest_framework import serializers
from api.models.roles import Roles

class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = ['roles_name', 'roles_status_check']
