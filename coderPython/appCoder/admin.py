from django.contrib import admin
from appCoder.models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Sold_items)
admin.site.register(Purchased_items)

