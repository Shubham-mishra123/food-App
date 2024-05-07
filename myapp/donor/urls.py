from django.urls import path,include
from . import views as v

urlpatterns =[
    path("donorhome",v.donorhome),
    path("add-food",v.addfood),
    path("delete-food/<int:pk>",v.deletefood),
    path("edit-food/<int:pk>",v.editfood),
    path("requests",v.requests),
    path("accept-request/<int:pk>",v.acceptrequest),
     path("reject-request/<int:pk>",v.rejectrequest)
    
]