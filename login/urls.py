
from django.urls import path
from . import views

urlpatterns = [
    
    path('index/',views.index,name="index"),
   
    path('Signuphandle/',views.Signuphandle,name="Signuphandle"),
    path('loginhandle/',views.loginhandle,name="loginhandle"),
    path('about/',views.about,name="about"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('sign/',views.sign,name="sign"),
    path('contact/',views.contact,name="contact"),
    path('logouthandle/',views.logouthandle,name="logouthandle"),
    path('Contacthandle/',views.Contacthandle,name="Contacthandle"),



]
