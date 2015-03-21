from django.db import models

# Create your models here.
from madmin.utils import *
from common import utils as comutils
import logging

#admin model
class Madmin(models.Model):
    adminname = models.CharField(max_length = 16, unique = True)
    passwd = models.CharField(max_length = 80)
    authority = models.CharField(max_length = 100, default="")
     
    def save(self):
        db_datas =  Madmin.objects.filter(passwd=self.passwd)
        #update passwd
        if len(db_datas) == 0:
            #encrypt passwd when data is inserted into DB
            self.passwd = comutils.encrypt(self.passwd)
        super(Madmin, self).save()
