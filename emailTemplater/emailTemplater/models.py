from django.db import models
from taggit.managers import TaggableManager

class TemplateForm(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.CharField(max_length=200)
  body = models.TextField(blank=True, )
  show_in_list = models.BooleanField(default=True)
  tags = TaggableManager(blank=True)

