from rest_framework import serializers
from api.models.modules import Modules
from api.setserializers.serializers_roles import RolesSerializer


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['modules_roles_dp', 'modules_created', 'modules_name','modules_permissions_checklist']