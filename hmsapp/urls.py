from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('home',views.home),
    path('register',views.register),
    path('signin',views.signin),
    path('orthodoc',views.orthodoc),
    path('outdoor',views.outdoor),
    path('paedidoc',views.paedidoc),
    path('cardiodoc',views.cardiodoc),
    path('gynaedoc',views.gynaedoc),
    path('entdoc',views.entdoc),
    path('slotbooksucc',views.slotbooksucc),
    path('reg_store',views.reg_store),
    path('show',views.show),
    path('check',views.check),
     path('access',views.access),
]