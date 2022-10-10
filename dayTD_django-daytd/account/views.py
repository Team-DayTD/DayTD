from django.shortcuts import render
# from .forms import RegisterForm
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import OurUser
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
# Create your views here.


class OurUserListAPI(APIView):
    def get(self, request):
        queryset = OurUser.objects.all()
        print(queryset)
        serializer = OurUserSerializer(queryset, many=True)
        return Response(serializer.data)


class RegisterListAPI(APIView):
    def post(self, request):
        user_serializer = OurUserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 사용자 정보
class UserListAPI(APIView):
    def get(self, request):
        user = request.GET.get('user')

        my_user = OurUser.objects.filter(user__in=[user]).order_by().last()
        user_serializer = OurUserSerializer(my_user)

        return Response(user_serializer.data)