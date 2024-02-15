from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import actress
from .permissions import IsAdminOrReadOnly
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models  import  *



class actressAPIList(generics.ListCreateAPIView):
    queryset = actress.objects.all()
    serializer_class = actressSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)
class actressAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = actress.objects.all()
    serializer_class = actressSerializer

class actressAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = actress.objects.all()
    serializer_class = actressSerializer
    permission_classes = (IsAdminOrReadOnly, )

