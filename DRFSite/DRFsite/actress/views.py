from django.shortcuts import render
from rest_framework import  generics
from .models import actress
from .serializers import actressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

class actressApiviewOld(APIView):
    def get(self, request):
        lst = actress.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self,request):
        post_new = actress.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})

class actressApiview(APIView):
    def get(self, request):
        w = actress.objects.all()
        return Response({'posts': actressSerializer(w, many= True).data})

    def post(self,request):
        serializer = actressSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        post_new = actress.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': actressSerializer(post_new).data})
# class actressApiview(generics.ListAPIView):
#    queryset = actress.objects.all()
#    serializer_class = actressSerializer

