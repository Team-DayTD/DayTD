from rest_framework import serializers
from .models import OurUser

class OurUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUser
        fields = "__all__"
        # fields = ['user_id', 'password', 'gender', 'birth', 'email']

        # user_id = serializer.CharField(max_length=40)
        # password = serializer.CharField(max_length=40)
        # gender = serializer.CharField(max_length=2)
        # birth = serializer.DateField()
        # email = serializer.EmailField(max_length=254)