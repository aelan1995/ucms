from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from api.models.roles import Roles
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this


# Create your models here.

'''
Use to create users with specific roles in order for the user to dynamically add new roles

'''

class MyUserManager(BaseUserManager):   
    def create_user(self, email, username, userprofile_roles_dp, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            userprofile_roles_dp=Roles.objects.get(id=userprofile_roles_dp),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, userprofile_roles_dp, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            userprofile_roles_dp,
            username=username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user        

class UserProfile(AbstractBaseUser):    
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        null=True
    )
    username = models.CharField(max_length=50, unique=True)
    userprofile_created = models.DateTimeField(auto_now_add=True)
    userprofile_roles_dp = models.ForeignKey(Roles, on_delete=models.CASCADE)
    userprofile_status = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','userprofile_roles_dp']

    def __str__(self):
        return self.email
    		
    class Meta:
        ordering = ['userprofile_created']

