from django.shortcuts import get_object_or_404, render
from .models import Book
from .forms import BookForm
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.

def book_list_view(request):
    template_name = "book/list.html"
    print(messages)
    context = { 'books': Book.objects.all() }
    return render(request, template_name, context )


def book_detail_view(request, pk):
    template_name = "book/detail.html"
    obj = get_object_or_404(Book, id=pk)
    context = { 'book': obj }
    return render(request, template_name, context )



class BookDeleteView(DeleteView, SuccessMessageMixin):
    template_name = "book/delete.html"
    model = Book
    success_url = "/book/list"
    success_message = "Book successfully deleted"




class BookCreateView(CreateView):
    model = Book
    # fields = "__all__"
    form_class = BookForm
    template_name = "book/create.html"
    success_url = "/book/list"
    success_message = "Book successfully added"

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)
    


class BookUpdateView(UpdateView):
    template_name = "book/update.html"
    model = Book
    # fields = "__all__"
    form_class = BookForm
    success_url = "/book/list"
    success_message = "Book updated successfully"