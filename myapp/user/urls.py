from django.urls import path,include
from . import views as v

urlpatterns =[
    path("userhome",v.home),
    path("viewfood/<int:pk>",v.foodview),
    path("sendrequest/<int:pk>",v.send_request)
    
]