from django.urls import path
from appCoder.views import *

urlpatterns = [
    path("", inicio),
    path("items/", item),
    path("sellers/", seller),
    path("users/", user),
    path("sold_items/", sold_items),
    path("purchased_items/", purchased_items),
]