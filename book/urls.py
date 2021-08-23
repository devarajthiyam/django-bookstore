from django.urls import path
from . import views

urlpatterns = [
    path('list', views.book_list_view, name='book-list-page'),
    path('<int:pk>', views.book_detail_view, name='book-detail-page'),
    path('create', views.BookCreateView.as_view(), name='book-create-page'),
]