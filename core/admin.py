from django.contrib import admin

from conversation.models import Conversation
# from notifications.models import Notifications
from reports.models import Report
from .models import Category, Product
from listing.models import Listing


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Conversation)
# admin.site.register(Notifications)
admin.site.register(Report)
admin.site.register(Listing)



