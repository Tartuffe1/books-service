# Create your views here.
from django.shortcuts import render, get_object_or_404
from books.models import Book
from django.template import RequestContext

from forms import BookForm, BookEditForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

# we'll use more complex filter conditions for search tool
from django.db.models import Q

from django.contrib.auth import get_user

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User

# all books from database 
def books(request):
    latest_book_list = Book.objects.all()
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/books.html', context)      
def category(request, book_category):
    args={}
    args['context_instance']=RequestContext(request)
    
    category_list = Book.objects.filter(category__contains=book_category)
    paginator = Paginator(category_list, 10) # Show 10 contacts per page

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
    
def oglasi_korisnika(request, book_user):

    korisnik = get_object_or_404(User, username=book_user)
    oglasi_korisnika_lista = Book.objects.filter(user=korisnik)
    
    paginator = Paginator(oglasi_korisnika_lista, 10) # Show 10 contacts per page
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
    
    args={}
    args.update(csrf(request))
    args['oglasi_korisnika_lista']= books
    args['context_instance']=RequestContext(request)
    args['book_user']=korisnik
    return render(request, 'books/oglasi_korisnika.html', args)
    
def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book.html',
                            {'book': book })

#page visitor is able to add book
def add_book(request):
   if request.method == 'POST':
      form=BookForm(request.POST, request.FILES)
      if form.is_valid():
         new_book = form.save(commit=False)
         # prirodno sam pokusavao samo sa request.user, ali to cini se nije MyProfile objekt, stoga
         # ovaj get_user
         new_book.user = get_user(request)
         new_book.save()
         return HttpResponseRedirect('/accounts/my_books/')
   else:  
      if request.user.is_authenticated():
         form=BookForm() 
      else:
         return HttpResponseRedirect('/')
   
   args={}
   args.update(csrf(request))
   args['form']= form
   args['context_instance']=RequestContext(request)
   return render(request, 'books/add_book.html', args)
   
def book_edit(request,book_id):
   old_book = get_object_or_404(Book, pk=book_id)
   if request.method == 'POST':
      form=BookForm(request.POST, request.FILES,instance=old_book)
      if form.is_valid():
         new_book = form.save(commit=False)
         # prirodno sam pokusavao samo sa request.user, ali to cini se nije MyProfile objekt, stoga
         # ovaj get_user
         new_book.user = get_user(request)
         new_book.save()
         return HttpResponseRedirect('/accounts/my_books/')
   else:  
      if request.user.is_authenticated():
         form=BookEditForm(instance=old_book) 
      else:
         return HttpResponseRedirect('/')
   
   args={}
   args.update(csrf(request))
   args['form']= form
   args['book']=old_book
   args['context_instance']=RequestContext(request)
   return render(request, 'books/book_edit.html', args)

def book_delete(request,book_id):  
   book = get_object_or_404(Book, pk=book_id)
   book.delete()   
   return HttpResponseRedirect('/accounts/my_books/')

def search(request):
   args={}
   args.update(csrf(request))
   
   if request.method == 'GET':
      search_text=request.GET['search_text']
   else:
      search_text=''
      
   search_list=Book.objects.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text))
   
   paginator = Paginator(search_list, 10) # Show 10 contacts per page

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
        
   args['search_list']= books
   return render(request, 'books/search_book.html', args)
