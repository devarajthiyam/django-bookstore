from django.urls import path
from . import views

urlpatterns = [
    path('list', views.book_list_view, name='book-list-page'),
    path('create', views.BookCreateView.as_view(), name='book-create-page'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='book-update-page'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='book-delete-page'),
    path('<int:pk>', views.book_detail_view, name='book-detail-page'),

]