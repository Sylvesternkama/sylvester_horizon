from django.contrib import admin

from conversation.models import Conversation
# from notifications.models import Notifications
from .models import Category, Product


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Conversation)
# admin.site.register(Notifications)

