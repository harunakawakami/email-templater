from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Template(models.Model):
  subject = models.CharField(max_length=100)
  body = models.TextField(blank=True)
  show_in_list = models.BooleanField(help_text='Yes = show the template in the list')
  tags = TaggableManager()