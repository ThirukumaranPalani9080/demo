#from django.contrib import models
from django.urls import path
from  . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
   path('admin/', views.login, name = 'login'),
   path('', views.login, name = 'login'),
   # path('admin/', admin.site.urls),
   path('dashboard/', views.dashboard, name = 'dashboard'),
   # path('login/',LoginView.as_view(), name='login'),
   path('register', views.register, name = 'register'),
   path('logout', views.logout, name='logout' ),
   path('admin/adduser', views.adduser, name = 'adduser'),
   path('admin/viewalluser', views.viewalluser, name='viewalluser'),
   path('admin/edituser', views.edituser, name='edituser'),
   path('admin/deleteuser', views.deleteuser, name='deleteuser')




]