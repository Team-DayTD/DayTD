from rest_framework import serializers
from .models import *

# 코디에서 지역 선택

class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

# 사용자 선택 지역
class MyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLocation
        fields = "__all__"

# 사용자 선택 코디스타일
class MyStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClotheStyle
        fields = "__all__"

# 코디 출력
class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"

# 코디 찜기능
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"