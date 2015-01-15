# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from books.models import Book

from forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    args={}
    args['context_instance']=RequestContext(request)
    
    latest_book_list = Book.objects.order_by("pub_date").reverse()
    paginator = Paginator(latest_book_list, 8) # Show 8 contacts per page

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
    
def kontakt(request, book_user):
    if request.method == 'POST':
        # Do maila cemo doci tako da prvo pozovemo pripadajuci User objekt, a potom
        # iz njega izvucemo njegovo svojstvo 'mail'
        user = get_object_or_404(User, username=book_user)
        mail_prima=user.email
        
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                [mail_prima]
            )
            return render(request, 'thanks.html', {"name": "thanks"}, )
    else:
        form = ContactForm()
    # Moramo ukljuciti i name parametar koji ce nam sacuvati osobu kojoj saljemo mail, bilo urednika
    # bilo nekog oglasivaca.
    return render(request, 'contact_form.html', {'form': form, "name": book_user}, )
    
