from django.shortcuts import render, redirect
from base.models import Books, Author, Categories,BookImage
from django.contrib.auth.decorators import login_required
from .forms import BookForm, BookImageForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.shortcuts import get_object_or_404

BookImageFormSet = inlineformset_factory(
    Books,
    BookImage,
    form=BookImageForm,
    extra=1,  # Number of additional empty forms to display
    can_delete=True  # Allow deleting images
)

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

@login_required
def my_book(request):
    books = Books.objects.prefetch_related('images').filter(created_by=request.user)
    return render(request, 'base/my_books.html', {"books": books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        formset = BookImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            formset.instance = book
            formset.save()
            messages.success(request, 'Book added successfully.')
            return redirect('my_book')  # Redirect to the book list or detail page
    else:
        form = BookForm()
        formset = BookImageFormSet()
    return render(request, 'base/add_book.html', {'form': form, 'formset': formset})


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Books, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        formset = BookImageFormSet(request.POST, request.FILES, instance=book)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
        formset = BookImageFormSet(instance=book)
    return render(request, 'base/edit_book.html', {'form': form, 'formset': formset})

