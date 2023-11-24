from django.db import models


# Create your models here.

'''
Permission - a page for creating permission based on the modules added
PermissionSelection - based on roles and what permissions on does he have

'''

class Permissions(models.Model):
    permissions_name = models.CharField(max_length=50, unique=True)
    permissions_created = models.DateTimeField(auto_now_add=True)
    permission_status_check = models.BooleanField(default=False)

    class Meta:
        ordering = ['permissions_created']

    def __str__(self):
        return self.permissions_name