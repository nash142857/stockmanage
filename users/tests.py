from django.test import TestCase
from django.shortcuts import render



def test_get_verify_code(request):
    return render(request, 'test_get_verify_code.html')


def test_check_verify_code(request):
    return render(request, 'test_check_verify_code.html')


def test_signup(request):
    return render(request, 'test_signup.html')

def test_signin(request):
    return render(request, 'test_signin.html')

def test_signout(request):
    return render(request, 'test_signout.html')

def test_reset_password(request):
    return render(request, 'test_reset_password.html')

def test_set_signature(request):
    return render(request, 'test_set_signature.html')

def test_set_verify(request):
    return render(request, 'test_set_verify.html')

def test_upload_avatar(request):
    return render(request, 'test_upload_avatar.html')
