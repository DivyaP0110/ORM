from django.db import models
from django.contrib import admin
class Footballplayers (models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.DateField()
    Height=models.IntegerField()
    Address=models.CharField(max_length=100)
    MobileNo=models.IntegerField()
class FootballplayersAdmin(admin.ModelAdmin):
    list_display=["Name","DOB","Height","Address","MobileNo"]
