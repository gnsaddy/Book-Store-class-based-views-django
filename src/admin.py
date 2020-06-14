from import_export.admin import ImportExportModelAdmin

from .models import Book
from django.contrib.auth.models import Group
from django.contrib import admin


# Register your models here.

class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'isbn_number', 'book_added')
    list_display_links = ('name',)
    list_editable = ('isbn_number',)
    list_per_page = 10
    search_fields = ('name', 'isbn_number')


admin.site.register(Book, BookAdmin)
admin.site.unregister(Group)
