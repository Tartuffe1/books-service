# Create your views here.
from django.shortcuts import render, get_object_or_404
from books.models import Book
from django.template import RequestContext

from forms import BookForm
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
    paginator = Paginator(category_list, 4) # Show 4 contacts per page

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
    
    args={}
    args.update(csrf(request))
    args['oglasi_korisnika_lista']= oglasi_korisnika_lista
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
         return HttpResponseRedirect('/')
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
  
def search(request):
   args={}
   args.update(csrf(request))
   
   if request.method == 'POST':
      search_text=request.POST['search_text']
   else:
      search_text=''
      
   search_list=Book.objects.filter(Q(title__contains=search_text) | Q(description__contains=search_text))
   
   paginator = Paginator(search_list, 4) # Show 4 contacts per page

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
   return render(request, 'books/search.html', args)
