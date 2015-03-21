from django.conf.urls import patterns, include, url
from users import views
from users import tests

urlpatterns = patterns('',
    
    url(r'^api/signup/$', views.signup, name = 'user_signup' ),
    url(r'^api/signin/$', views.signin, name = 'user_signin' ),
    url(r'^api/signout/$', views.signout, name = 'user_signout' ),
    url(r'^api/check_verify_code/$', views.check_verify_code, name = 'user_check_verify_code' ),
    url(r'^api/get_verify_code/$', views.get_verify_code, name = 'user_get_verify_code' ),
    url(r'^api/upload_avatar/$', views.upload_avatar, name = 'user_upload_avatar' ),
    url(r'^api/set_signature/$', views.set_signature, name = 'user_set_signature' ),
    url(r'^api/set_verify/$', views.set_verify, name = 'user_set_verify' ),
    url(r'^api/reset_password/$', views.reset_password, name = 'user_reset_password' ),
    
    
    url(r'^check_login/$', views.check_login),
    url(r'^test/signup/$', tests.test_signup),
    url(r'^test/signin/$', tests.test_signin),
    url(r'^test/signout/$', tests.test_signout),
    url(r'^test/get_verify_code/$', tests.test_get_verify_code),
    url(r'^test/check_verify_code/$', tests.test_check_verify_code),
    url(r'^test/upload_avatar/$', tests.test_upload_avatar),
    url(r'^test/set_signature/$', tests.test_set_signature),
    url(r'^test/set_verify/$', tests.test_set_verify),
    url(r'^test/reset_password/$', tests.test_reset_password),
)
