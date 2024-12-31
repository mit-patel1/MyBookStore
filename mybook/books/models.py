from django.db import models
from django.contrib.auth.models import User
import os
import re
from django.conf import settings
from datetime import datetime


def sanitize_filename(name):
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')

def book_image_upload_to(instance, filename):
    # Generate a custom path: "books/<book_title>/images/<filename>"
    sanitized_title = sanitize_filename(instance.book.name)
    base, ext = os.path.splitext(filename)
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    return f"book_images/{year}/{month}/{day}/{sanitized_title}_{instance.book.id}/{base}{ext}"

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class MyBook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, verbose_name='author')
    category = models.ManyToManyField(BookCategory, verbose_name='category')
    purchase_link = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class BookImage(models.Model):
    book = models.ForeignKey(MyBook, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=book_image_upload_to)

    def __str__(self):
        return f"Image for {self.book.name}"