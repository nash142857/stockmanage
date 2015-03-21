from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime

import re
import json

#phone_regex = RegexValidator(regex = r'^\d{11}$', message = 'phone number must be the format '12345678901' 11 digits')

class User(models.Model):
    phone = models.CharField(max_length = 12, unique = True)
    nick_name = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 64)
    is_verify = models.BooleanField(default = False)
    avatar = models.CharField(max_length = 64, blank = True)
    date_joined = models.DateTimeField(default = datetime.now, blank = True)
    signature = models.CharField(max_length = 100, blank = True)

#    def __unicode__(self):
#        return json.dumps(dict(phone = self.phone,
#                                nick_name = self.nick_name,
#                                is_verify = self.is_verify,
#                                avatar = self.avatar,
#                                date_joined = self.date_joined,
#                                signature = self.signature), ensure_ascii = False).decode('utf-8')
#
    def __unicode__(self):
        return json.dumps(dict(phone = self.phone,
                                nick_name = self.nick_name,
                                is_verify = self.is_verify,
                                avatar = self.avatar,
                                date_joined = str(self.date_joined),
                                signature = self.signature), ensure_ascii = False)

    def __str__(self):
        return unicode(self).encode('utf-8')


#    def clean(self, *args, **kwargs):
#        ## add user valid
#        if not re.match(r'^[\w\d-\u4e00-\u9fa5]{2, 10}$', self.nickname):
#            raise ValidationError(u'nick name invalid')
#        if not re.match(r'^\d{11}$', self.phone):
#            raise ValidationError(u'phone invalid')
#        super(User, self).clean(*args, **kwargs)
#
#    
#    def save(self, *args, **kwargs):
#        self.full_clean()
#        super(User, self).save(*args, **kwargs)
