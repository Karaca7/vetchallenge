
from django.contrib import admin
from django.urls import path
from userpage import views


urlpatterns = [
        path("",views.Userp,name="main"),
        path("addpet/",views.Addpet,name="addpet"),
        path("addpetowner/",views.AddPetOwner,name="addpetowner"),

    
    
]
    
