from django.urls import path
from django.conf.urls.static import static 

from . import views

urlpatterns = [
    path ('',views.home, name=""),
    path ('register',views.register, name="register"),
    path ('my-login',views.my_login, name="my-login"),
   
    path('user-logout', views.user_logout, name="user-logout",),

#curd
    path ('dashboard',views.dashboard, name="dashboard")


]