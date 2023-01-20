from django.db import models

class Template(models.Model):
  id = models.AutoField(primary_key=True)
  subject = models.CharField(max_length=200)
  body = models.CharField(max_length=5000, blank=True, null=True)
  show_in_list = models.BooleanField(default=True)

class Category(models.Model):
  