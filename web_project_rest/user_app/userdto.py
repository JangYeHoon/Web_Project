from rest_framework import serializers, viewsets
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'name_ko', 'name_eng',
            'call', 'passport', 'country', 'birthday', 'sex']