from django.contrib import admin

from .models import signup,cart,ContactMessage
admin.site.register(signup)
admin.site.register(cart)
admin.site.register(ContactMessage)