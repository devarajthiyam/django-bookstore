from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.

def book_list_view(request):
    template_name = "book/list.html"
    context = { 'books': Book.objects.all() }
    print(context)
    return render(request, template_name, context )


def book_detail_view(request, pk):
    template_name = "book/detail.html"
    obj = get_object_or_404(Book, id=pk)
    context = { 'book': obj }
    return render(request, template_name, context )