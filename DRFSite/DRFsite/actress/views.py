from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action

from .models import actress
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class ActressViewSet(viewsets.ModelViewSet):
    # queryset = actress.objects.all()
    serializer_class = actressSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return actress.objects.all()[:3]

        return actress.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class actressApiviewOld(APIView):
#     def get(self, request):
#         lst = actress.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def post(self,request):
#         post_new = actress.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id = request.data['cat_id']
#         )
#
#         return Response({'post': model_to_dict(post_new)})

# class actressAPIList(generics.ListCreateAPIView):
#     queryset = actress.objects.all()
#     serializer_class = actressSerializer
#
# class actressAPIUpdate(generics.UpdateAPIView):
#     queryset = actress.objects.all()
#     serializer_class = actressSerializer
#
# class actressAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = actress.objects.all()
#     serializer_class = actressSerializer

# class actressApiview(APIView):
#     def get(self, request):
#         w = actress.objects.all()
#         return Response({'posts': actressSerializer(w, many= True).data})
#
#     def post(self,request):
#         serializer = actressSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args , **kwargs ):
#         pk = kwargs.get("pk", None)
#         if not pk :
#             return Response({"error": "method put is not allowed"})
#
#         try:
#             instance = actress.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exists"})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "method DELETE is not allowed"})
#
#         return Response({"post": "delete post"+ str(pk)})
#
#
#
#
#         serializer = actressSerializer(data= request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#

# class actressApiview(generics.ListAPIView):
#    queryset = actress.objects.all()
#    serializer_class = actressSerializer
