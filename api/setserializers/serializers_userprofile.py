from api.models.userprofile import UserProfile
from api.models.userprofile import User
from rest_framework import serializers

# Serializers define the API representation.

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='userprofile',
        lookup_field='slug'
    )
    userprofile_user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username',
        many=True,
        read_only=True
    )
    class Meta:
        model = UserProfile
        fields = ['url', 'id','userprofile_user','userprofile_created','userprofile_roles_dp','userprofile_status']
    



