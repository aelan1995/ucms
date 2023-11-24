from django.db import models
from .roles import Roles
from .permissions import Permissions

# Create your models here.

'''
Modules - allows you roles and permission to a certain module you created.

'''

class Modules(models.Model):
    modules_roles_dp = models.ForeignKey(Roles, on_delete=models.CASCADE)
    modules_created = models.DateTimeField(auto_now_add=True)
    modules_name = models.CharField(max_length=50, unique=True)
    modules_permissions_checklist = models.ManyToManyField(Permissions)

    class Meta:
        ordering = ['modules_created']
