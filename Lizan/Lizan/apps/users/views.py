from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
# POST /users/
from . import serializers
from .models import User


# POST users/
class UserView(CreateAPIView):
    """
    用户注册
    传入参数：
        username, password, password2, sms_code, mobile, allow
    """
    # 指定序列化器
    serializer_class = serializers.UserSerializer


# GET /username/(?P<username>\{5, 20}/count/, views.UsernameCountView.as_view()
class UsernameCountView(APIView):
    """验证用户名是否已存在"""

    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        data = {
            'count': count,
            'username': username
        }
        return Response(data)
