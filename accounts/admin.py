__author__ = 'hari'
from django.contrib import admin
from models import MyCustomProfile
from userena.utils import get_user_model,get_profile_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from userena.admin import UserenaAdmin,UserenaSignupInline

class MyCustomProfileAdmin(admin.ModelAdmin):
    list_display = ["user" ,"bio","my_legacy_user_object"]
    search_fields = ["user__first_name","user__last_name","my_legacy_user_object"]

#docs from https://github.com/bread-and-pepper/django-userena/blob/master/docs/faq.rst
admin.site.unregister(get_profile_model())
admin.site.register(MyCustomProfile,MyCustomProfileAdmin)

class MyCustomProfileAdminInline(admin.StackedInline):
    model = MyCustomProfile


class MyCustomProfileAddedAdmin(UserenaAdmin):
    inlines = [UserenaSignupInline,MyCustomProfileAdminInline]

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(),MyCustomProfileAddedAdmin)