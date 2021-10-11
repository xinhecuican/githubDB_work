#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context, loader

def home(request):
    template = '%shome.html' %settings.TEMPLATE_DIRS
    return render_to_response(template)
