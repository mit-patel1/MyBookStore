from django.contrib import admin
from django.urls import path
from base import views as base_view
from accounts import views as account_view
app = 'accounts'

urlpatterns = [
    path('login/', account_view.login, name='login'),
    path('register/', account_view.register, name='register'),
]
