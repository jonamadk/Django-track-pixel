from django.db import models
from django.db.models.fields import CharField, EmailField, UUIDField
import random
# Create your models here.


class UserModel(models.Model):
    email = EmailField(max_length = 254 , blank= True , null=True)
    counter_is = CharField(max_length = 242, blank = True , null = True)
    unique_code = UUIDField(null=True, blank=True , unique=True)
    

    def __str__(self):
        return self.email