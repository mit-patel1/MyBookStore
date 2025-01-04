from django.contrib import admin
from django.urls import path
from accounts import views as account_view
app = 'accounts'

urlpatterns = [
    path('login/', account_view.login_request, name='login'),
    path('logout/', account_view.logout_request, name='logout'),
    path('register/', account_view.register_request, name='register'),
]
