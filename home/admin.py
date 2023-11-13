# Register your models here.

from django.contrib import admin
from home.models import Setting, ContactFormMessage, UserProfile, FAQ


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'country', 'image_tag']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Setting)
admin.site.register(FAQ, FAQAdmin)
