from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.db.models.manager import Manager
from django.contrib.auth.models import AbstractBaseUser

# class CustomAccountManager(BaseUserManager):

#     def createUser(self, username, password, **otherfields):
#         user = self.model(username=username, password = password)
#         user.set_password(password)
#         user.save()
#         return user

# class Adduser( PermissionsMixin):
#     username = models.CharField(max_length=50, unique= True)
#     password = models.CharField(max_length = 25)
#     #is_admin = models.BooleanField(default = False)
#     is_superuser = models.BooleanField(default=False)
#     'REQUIRED_FIELD' = [username]

#     def __str__(self):
#         return self.username

class Myuser(models.Model):  
    username = models.CharField(max_length=20)   
    eemail = models.EmailField()  
    password = models.CharField(max_length=100) 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username',]
    # econtact = models.CharField(max_length=15)  
    class Meta: 
        abstract = False 
        db_table = "myuser" 

