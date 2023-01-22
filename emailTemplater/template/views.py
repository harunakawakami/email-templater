from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Template
from template.serializers import UserSerializer, GroupSerializer, TemplateSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST'])
def template_list(request):

  if request.method == 'GET':
      templates = Template.objects.all()
      serializer = TemplateSerializer(templates, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)


  if request.method == 'POST':
      serializer =  TemplateSerializer(data=request.data)
      if serializer .is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def template_detail(request, id):

    try:
      template = Template.objects.get(pk=id)
    except Template.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = TemplateSerializer(template)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
      serializer = TemplateSerializer(template, data=request.data)
      if serializer .is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      template.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
 
