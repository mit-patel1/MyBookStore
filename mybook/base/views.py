from django.shortcuts import render
from base.models import Books, Author, Categories

# Create your views here.

def index(request):
    books = Books.objects.prefetch_related('images').all()
    return render(request, 'base/home.html', {"books": books})


def book_detail(request, book_id):
    # book_datas = Books.objects.prefetch_related('images').get(id=book_id)
    book_datas = Books.objects.prefetch_related('images').filter(id=book_id).first()
    return render(request, 'base/book_details.html', {"book_datas": book_datas})

def categories_wise_books(request, category_id):
    books = Books.objects.prefetch_related('images').filter(category = category_id)
    return render(request, 'base/home.html', {"books": books})