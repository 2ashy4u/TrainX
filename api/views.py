from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
        self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        # Enter information for classes
        if serializer.is_valid():
            pass
