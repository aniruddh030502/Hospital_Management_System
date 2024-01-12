from django.db import models

# Create your models here.
class user_reg(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    E_mail=models.EmailField()
    Date_of_Birth=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    class Meta:
        db_table="User_Registration"
class doct_dept(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    Doctor_id=models.CharField(max_length=5)
    class Meta:
        db_table="Doctor_Department"       
class doct_Johnson(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Doctor_date=models.CharField(max_length=50)
    cnt=models.IntegerField(max_length=50)
    class Meta:
        db_table="Doctor_Johnson" 
class doct_Jenny(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Doctor_date=models.CharField(max_length=50)
   # cnt=models.IntegerField(max_length=50)
    class Meta:
        db_table="Doctor_Jenny"    
class doct_Smith(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Doctor_date=models.CharField(max_length=50)
   # cnt=models.IntegerField(max_length=50)
    class Meta:
        db_table="Doctor_Smith"    
class doct_David(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Doctor_date=models.CharField(max_length=50)
   # cnt=models.IntegerField(max_length=50)
    class Meta:
        db_table="Doctor_David"    
class doct_Hopkin(models.Model):
    Doctor_Name=models.CharField(max_length=50)
    Doctor_date=models.CharField(max_length=50)
   # cnt=models.IntegerField(max_length=50)
    class Meta:
        db_table="Doctor_Hopkin"       

class Bed_Details(models.Model):
    bed_Number=models.CharField(max_length=50)
   # BedNo=models.CharField(max_length=123)
    Status=models.CharField(max_length=50)
    class   Meta:
        db_table="Bed_Details_List"
class Bed_Apply(models.Model):
    Name=models.CharField(max_length=50)
    ContactNo=models.CharField(max_length=50)
    Comments=models.CharField(max_length=50)
    is_approved = models.CharField(max_length=50,default="Vacant")
    BedNo=models.IntegerField(max_length=123,default=0)
class Bed_Confirm(models.Model):
    Name=models.CharField(max_length=50)
    ContactNo=models.CharField(max_length=50)
    Comments=models.CharField(max_length=50)
    #is_approved = models.CharField(max_length=50,default="Vacant")
   # BedNo=models.CharField(max_length=123)