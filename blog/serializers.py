from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User, Group

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body']
