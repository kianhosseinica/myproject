from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('business/', views.business_info, name='business_info'),
    path('manychat/webhook/', views.manychat_webhook, name='manychat_webhook'),
]
