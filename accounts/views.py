from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib.auth.forms import UserCreationForm

from django.template import RequestContext

from accounts.forms import ChangeEmailForm
from django.contrib.auth.forms import PasswordChangeForm

from books.models import Book

def login(request):
   c={}
   c.update(csrf(request))
   return render(request, 'accounts/signin_form.html',c) 
   
def auth_view(request):
   username=request.POST.get('username','')
   password=request.POST.get('password','')
   user=auth.authenticate(username=username, password=password)
   
   if user is not None:
     auth.login(request, user)
     return HttpResponseRedirect('/accounts/loggedin/')
   else:
     return HttpResponseRedirect('/accounts/invalid/')
     
def loggedin(request):
   return render(request,'home2.html',context_instance=RequestContext(request))
                             
def invalid_login(request):
   return render(request,'accounts/activate_fail.html',context_instance=RequestContext(request))
   
def logout(request):
   auth.logout(request)
   return render(request,'home2.html', context_instance=RequestContext(request))
   
def register_user(request):
   if request.method == 'POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/accounts/register_success/')
      
   args={}
   args.update(csrf(request))
   args['form']=UserCreationForm()
   args['context_instance']=RequestContext(request)
   return render(request,'accounts/signup_form.html',args)
   
def register_success(request):
   return render_to_response('accounts/signup_complete.html')

def profile_detail(request):
    return render(request,'accounts/profile_detail.html', context_instance=RequestContext(request))
    
def profile_edit(request):
    return 
def email_change(request, username, email_form=ChangeEmailForm,
                 template_name='userena/email_form.html', success_url=None,
                 extra_context=None):
    return
    
def password_change(request):
    if request.method == 'POST':
      form = PasswordChangeForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/accounts/register_success/')
      
    args={}
    args.update(csrf(request))
    args['form']=PasswordChangeForm(request)
    args['context_instance']=RequestContext(request)
    return render(request,'accounts/password_form.html',args)
    
def my_books(request):
    my_books_list = Book.objects.filter(user=request.user)
    
    args={}
    args.update(csrf(request))
    args['my_books_list']= my_books_list
    args['context_instance']=RequestContext(request)
    return render(request, 'accounts/my_books.html', args)