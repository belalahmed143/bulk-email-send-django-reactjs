from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=200)
    message  = serializers.CharField(max_length=1000)
    