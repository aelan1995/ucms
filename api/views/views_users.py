# ViewSets define the view behavior.
from api.models.userprofile import UserProfile
from rest_framework import viewsets
from api.setserializers.serializers_userprofile import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
