from django.contrib.auth.models import User, Group
from .models import Template
from rest_framework import serializers
from taggit.serializers import TagListSerializerField,TaggitSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class TemplateSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Template
        fields = ['id', 'subject', 'body', 'show_in_list', 'tags']