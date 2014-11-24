# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from books.models import Book

def home(request):
    args={}
    latest_book_list = Book.objects.all()
    args['latest_book_list']=latest_book_list
    args['context_instance']=RequestContext(request)
    return render(request, 'home.html', args)
    
