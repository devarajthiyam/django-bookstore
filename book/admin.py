from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book
    
    list_display = ['title', 'publish_date', 'author_full_name']
    search_fields = ['title']
    list_filter = ['author_full_name']


# Register your models here.
admin.site.register(Book, BookAdmin)
