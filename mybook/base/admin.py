from django.contrib import admin
from base.models import Categories,Author,Books, BookImage

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class BookImageInline(admin.StackedInline):
    model = BookImage
    extra = 1

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    inlines = [BookImageInline]


admin.site.register(BookImage)