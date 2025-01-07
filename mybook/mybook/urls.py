"""
URL configuration for mybook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base import views as base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("accounts.urls")),
    path('', base_view.index, name='home'),
    path('my_book/', base_view.my_book, name='my_book'),
    path('book_detail/<int:book_id>/', base_view.book_detail, name='Details'),
    path('books/<int:category_id>/', base_view.categories_wise_books, name='books'),
    path('accounts/', include('accounts.urls')),
    path('add/', base_view.add_book, name='add_book'),
    path('<int:pk>/edit/', base_view.edit_book, name='edit_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
