from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib.auth.forms import UserCreationForm

from django.template import RequestContext

from accounts.forms import UserForm, UserProfileForm, UpdateProfile
#Zelim da korisnik moze promijeniti password.
from django.contrib.auth.forms import PasswordChangeForm

from books.models import Book

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
   # Ovaj kod ispod posudjen je iz myheroku.views.home, ponavlja se i ispod u def logout, mogao bih ga ukljuciti
   # sa necim poput include
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
                             
def invalid_login(request):
   return render(request,'accounts/activate_fail.html',context_instance=RequestContext(request))
   
def logout(request):
   auth.logout(request)
   
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
   
def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'mobitel' in request.POST:
                profile.mobitel = request.POST['mobitel']
            if 'zupanija' in request.POST:
                profile.zupanija = request.POST['zupanija']

            # Now we save the UserProfile model instance.
            profile.save()
            
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'accounts/signup_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
def register_success(request):
   return render_to_response('accounts/signup_complete.html')

def profile_detail(request):
    args={}
    args.update(csrf(request))
    args['context_instance']=RequestContext(request)
    return render(request,'accounts/profile_detail.html', args)
    
def profile_edit(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    updated = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UpdateProfile(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.save()
            
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'mobitel' in request.POST:
                profile.mobitel = request.POST['mobitel']
            if 'zupanija' in request.POST:
                profile.zupanija = request.POST['zupanija']

            # Now we save the UserProfile model instance.
            profile.save()
            
            # Update our variable to tell the template registration was successful.
            updated = True
                
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UpdateProfile(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    # Render the template depending on the context.
    return render(request,
            'accounts/profile_edit_form.html',
            {'user_form': user_form, 'profile_form': profile_form, 'updated': updated} )

def my_books(request):
    my_books_list = Book.objects.filter(user=request.user)
    
    args={}
    args.update(csrf(request))
    args['my_books_list']= my_books_list
    args['context_instance']=RequestContext(request)
    return render(request, 'accounts/my_books.html', args)
    
def email_change(request):
    return
    
def password_change(request):
    if request.method == 'POST':
      # Ovo user=request.user je neophodno za djangovu PasswordChangeForm kada zelimo
      # da promijeni zaporku odredjenog Usera!
      form = PasswordChangeForm(user=request.user, data=request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/accounts/password_change_complete/')
      
    args={}
    args.update(csrf(request))
    args['form']=PasswordChangeForm(request)
    args['context_instance']=RequestContext(request)
    return render(request,'accounts/password_form.html',args)
    
def password_change_complete(request):
    #Ne znam da li mi je ovaj args potreban ovdje?
    args={}
    args.update(csrf(request))
    args['context_instance']=RequestContext(request)
    return render(request,'accounts/password_complete.html',args)