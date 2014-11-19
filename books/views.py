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

# all books from database 
def books(request):
    latest_book_list = Book.objects.all()
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/books.html', context)      

# specific book from database
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
         new_book.user = request.user
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
#searching books by category
def category(request, book_category):
  args={}
  args.update(csrf(request))
  
  category_list = Book.objects.filter(category__contains=book_category)
   
  args['category_list']= category_list
  return render(request, 'books/category.html', args)
  
def search(request):
   if request.method == 'POST':
      search_text=request.POST['search_text']
   else:
      search_text=''
      
   books=Book.objects.filter(Q(title__contains=search_text) | Q(author__contains=search_text))
   
   return render(request,'books/search.html',{'books_found': books})
