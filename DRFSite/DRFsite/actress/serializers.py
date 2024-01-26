import io

from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class ActressModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class actressSerializerold(serializers.ModelSerializer):
    class Meta:
        model = actress
        fields = ('title', 'cat_id')

class actressSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

# def encode():
#     model = ActressModel('Margot Robbie', 'Margot Robbie')
#     model_sr = actressSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep= '\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Margot Robbie", "content":"Content:Margot Robbie"}')
#     data = JSONParser().parse(stream)
#     serializer = actressSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)