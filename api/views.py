# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

import jwt
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Permission, Group
from api.forms import *
from api.models import *


def index(request):
    return HttpResponse("epedidos api")

@csrf_exempt
def signup(request):
    if request.method == 'GET':
        register_form = RegisterForm(data=request.GET)
        if register_form.is_valid():
            try:
                register = register_form.save()
                register.set_password(register.password)
                register.save()
                user = User.objects.filter(pk=register.pk)
                user_serializer = serializers.serialize("json", user)
                token = jwt.encode({request.GET.get('username',False): request.GET.get('password',False)}, 'secret', algorithm='HS256')
                a = AccountSystem()
                a.name = request.GET.get('name',False)
                a.save()
                user_profile = UserProfile()
                user_profile.user = User.objects.get(pk=register.pk)
                user_profile.access_token = token
                user_profile.account_system = a
                user_profile.save()
                return HttpResponse('[{"token":"'+token+'", "data":"'+user_serializer+'"}]')
            except:
                return HttpResponse('500')
        else:
            return HttpResponse(register_form.errors)