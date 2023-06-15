from django.contrib import admin
from .models import BookAuthor, Book
from import_export.admin import ImportExportActionModelAdmin



class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ("title","slug", "year", "price", "is_special", "is_trending")


@admin.register(BookAuthor)
class BookAuthorAdmin(ImportExportActionModelAdmin):
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "year", "author", "price", "is_special", "is_trending")
    list_filter = ("is_special", "is_trending", "author")
    search_fields = ("title", "author__name", "year", "description", "author__bio")
    prepopulated_fields = {"slug": ("title",)}
