from django.db import models

class reg(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    E_mail=models.EmailField(primary_key=True)
    Date_of_Birth=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
class pleasetablebanao(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    E_mail=models.EmailField(primary_key=True)
    Date_of_Birth=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
