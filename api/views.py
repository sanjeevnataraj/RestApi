from django.shortcuts import render
from api.models import User, ActivityPeriod
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import UserSerializer, ActivePeriodSerializer

class UserDetail(ListAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset.all(), many=True)
        return Response({'ok':True,'members':serializer.data})
