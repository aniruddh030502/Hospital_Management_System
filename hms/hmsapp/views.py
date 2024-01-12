from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#from .forms  import *
# Create your views here.

def index(request):
    return  HttpResponse('<h1>HelloWorld</h1>')
def home(request):
   return render(request,'home.html')
def register(request):
   return render(request,'register.html')
def signin(request):
   return render(request,'signin.html')
def orthodoc(request):
   return render(request,'orthodoc.html')
def outdoor(request):
   return render(request,'outdoor.html')
def cardiodoc(request):
   return render(request,'cardiodoc.html')
def gynaedoc(request):
   return render(request,'gynaedoc.html')
def paedidoc(request):
   return render(request,'paedidoc.html')
def entdoc(request):
   return render(request,'entdoc.html')
def slotbooksucc(request):
   return render(request,'slotbooksucc.html')
def reg_store(request):
    u=user_reg()
    u.First_Name=request.GET['a1']
    u.Last_Name=request.GET['a2']
    u.E_mail=request.GET['a3']
    u.Date_of_Birth=request.GET['a4']
    u.Username=request.GET['a5']
    u.Password=request.GET['a6']
    u.Gender=request.GET['a7']
    u.Address=request.GET['a8']
    u.save()
    return render(request,'signin.html')
def show(request):
    u=user_reg.objects.all()
    return render(request,'show.html',{'a':u})
def check(request):
   a=request.GET['username']
   b=request.GET['password']
   if(a=='admin'  and   b=="12345"):
      return  render(request,'admin_access.html') 
   if user_reg.objects.filter(E_mail=a,Password=b):
      #x=user_reg.objects.get(email=a)
      return render(request,'access.html')
   else:
      return render(request,'signin.html')     
def  access(request):
   return render(request,'access.html')  
def   slot_johnson(request):
   r=doct_Johnson()  
   a=request.GET['day']
   
   if doct_Johnson.objects.filter(Doctor_date=a[0:15]):
     print("True")
   r.Doctor_Name="joo"
   r.Doctor_date=request.GET['day'][0:15]
   #a=r.cnt
   r.cnt=1
   r.save()
   #print(cnt)
   return   render(request,'slotbooksucc.html')
def   slot_jenny(request):
   r=doct_Jenny()  
   a=request.GET['slot']
   
   if doct_Johnson.objects.filter(Doctor_date=a[0:15]):
     print("True")
   r.Doctor_Name="jen"
   r.Doctor_date=request.GET['slot'][0:15]
   #a=r.cnt
   r.cnt=1
   r.save()
   #print(cnt)
   return   render(request,'slotbooksucc.html')
def   slot_smith(request):
   r=doct_Smith()  
   a=request.GET['slot']
   
   #if doct_Smith.objects.filter(Doctor_date=a[0:15]):
     #print("True")
   r.Doctor_Name="jen"
   r.Doctor_date=request.GET['slot'][0:15]
   r.save()
   return   render(request,'slotbooksucc.html')
def   slot_david(request):
   r=doct_David()  
   a=request.GET['slot']
   
   #if doct_Smith.objects.filter(Doctor_date=a[0:15]):
     #print("True")
   r.Doctor_Name="jen"
   r.Doctor_date=request.GET['slot'][0:15]
   r.save()
   return   render(request,'slotbooksucc.html')
def   slot_hopkin(request):
   r=doct_Hopkin()  
   a=request.GET['slot']
   
   #if doct_Smith.objects.filter(Doctor_date=a[0:15]):
     #print("True")
   r.Doctor_Name="jen"
   r.Doctor_date=request.GET['slot'][0:15]
   r.save()
   return   render(request,'slotbooksucc.html')
def   bed_details(request):
   u=Bed_Details.objects.all()
   return render(request,'bed_details.html',{'a':u})
def   bed_apply(request):
   return render(request,'bed_apply.html')
def   submit_bed_application(request):
   u=Bed_Apply()
   u.Name=request.GET['name']
   u.ContactNo=request.GET['contact']
   u.Comments=request.GET['comments']
   u.save()
   return render(request,'bedbookappdone.html')
def   bedbookappdone(request):
   return render(request,'bedbookappdone.html')

def showbedapp(request):
    u=Bed_Apply.objects.all()
    return render(request,'showbedapp.html',{'a':u})

def bed_discharge(request):
    u=Bed_Confirm.objects.all()
    return render(request,'bed_discharge.html',{'a':u})

def   approve(request,id,name,comm,contact):
   bed_request =Bed_Confirm()
  # bed_request.Name=request.GET('Name')
   bed_request.is_approved ="Reserved"
   bed_request.Name=name
   bed_request.Comments=comm
   bed_request.ContactNo=contact
   bed_request.save()
   bd=Bed_Apply.objects.get(id=id)
   bd.delete()
   return render(request,'bedbooksucc.html')
def   discharge(request,id):
   bed_request=Bed_Confirm.objects.get(id=id)
   bed_request.delete()
 #  bed_request.save()
   return render(request,'dissucc.html')   
def   bedbooksucc(request):
   return   render(request,"bedbooksucc.html")
def   dissucc(request):
   return   render(request,"dissucc.html")
