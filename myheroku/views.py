# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
def home(request):
    args={}
    args['context_instance']=RequestContext(request)
    return render(request, 'home2.html', args)
