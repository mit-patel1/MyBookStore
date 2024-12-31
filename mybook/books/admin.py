from django.contrib import admin
from books.models import BookCategory,Author,MyBook, BookImage

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class BookImageInline(admin.StackedInline):
    model = BookImage
    extra = 1

@admin.register(MyBook)
class MyBookAdmin(admin.ModelAdmin):
    inlines = [BookImageInline]


admin.site.register(BookImage)