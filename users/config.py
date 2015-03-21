#! -*- coding:utf-8 -*-

from django.conf import settings

import os



SIGNUP_VERIFY_CODE_EXPIRE = 120
UPLOAD_AVATAR_DIR = os.path.join(settings.MEDIA_ROOT, 'avatar')

