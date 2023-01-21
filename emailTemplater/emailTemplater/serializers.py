from rest_framework import serializers
from .models import TemplateForm

class TemplateFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = TemplateForm
    fields = ['id', 'subject', 'body', 'show_in_list', 'tags']