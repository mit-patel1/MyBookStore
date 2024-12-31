from django.shortcuts import render
from books.models import MyBook, Author, BookCategory

# Create your views here.

def index(request):
    books = MyBook.objects.prefetch_related('images').all()
    return render(request, 'base/home.html', {"books": books})


def book_detail(request, book_id):
    # book_datas = MyBook.objects.prefetch_related('images').get(id=book_id)
    book_datas = MyBook.objects.prefetch_related('images').filter(id=book_id).first()
    print('book_datas', book_datas)
    return render(request, 'base/book_details.html', {"book_datas": book_datas})