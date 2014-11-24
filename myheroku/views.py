# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from books.models import Book

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    args={}
    args['context_instance']=RequestContext(request)
    
    latest_book_list = Book.objects.all()
    paginator = Paginator(latest_book_list, 4) # Show 4 contacts per page

    # this value is delivered by a href='?page=..., obviously it is GET method   
    page = request.GET.get('page')
    try:
       books = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer, deliver first page.
       books = paginator.page(1)
    except EmptyPage:
       # If page is out of range (e.g. 9999), deliver last page of results.
       books = paginator.page(paginator.num_pages)
        
    args['book_list']=books
    return render(request, 'home.html', args)
    
