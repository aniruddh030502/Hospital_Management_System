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
    u=pleasetablebanao()
    u.First_Name=request.GET['a1']
    u.Last_Name=request.GET['a2']
    u.E_mail=request.GET['a3']
    u.Date_of_Birth=request.GET['a4']
   #  u.Username=request.GET['a5']
    u.Password=request.GET['a6']
    u.Gender=request.GET['a7']
    u.Address=request.GET['a8']
    try:  
      x=pleasetablebanao.objects.get(E_mail=request.GET['a3'])
      if x is not None:
         return render(request,'register.html',{'a':"Email id already used"})
    except:
      u.save()
    return render(request,'signin.html')
def show(request):
    u=pleasetablebanao.objects.all()
    return render(request,'show.html',{'a':u})
def check(request):
   a=request.GET['username']
   b=request.GET['password']
   if pleasetablebanao.objects.filter(E_mail=a,Password=b):
      #x=pleasetablebanao.objects.get(email=a)
      return render(request,'access.html')
   else:
      return render(request,'signin.html')     
def  access(request):
   return render(request,'access.html')         

