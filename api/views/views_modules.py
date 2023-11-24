# ViewSets define the view behavior.
from api.models.modules import Modules
from rest_framework import viewsets
from api.setserializers.serializers_modules import ModulesSerializer

class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer
