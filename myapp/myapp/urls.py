
from django.contrib import admin
from django.urls import path,include
from user.views import loginpage,signup,logoutuser
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",loginpage),
    path("signup",signup),
    path('admin/', admin.site.urls),
    path("logout",logoutuser),
    path("",include("user.urls")),
    path("",include("donor.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
