# ViewSets define the view behavior.
from api.models.permissions import Permissions
from rest_framework import viewsets
from api.setserializers.serializers_permissions import PermissionsSerializer

class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
