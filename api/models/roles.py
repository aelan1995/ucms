from django.db import models

# Create your models here.

'''
Use to create roles in order for the user to dynamically add new roles

'''

class Roles(models.Model):
    roles_name = models.CharField(max_length=50, unique=True)
    roles_created = models.DateTimeField(auto_now_add=True)
    roles_status_check = models.BooleanField(default=False)

    class Meta:
        ordering = ['roles_created']

    def __str__(self):
        return self.roles_name
