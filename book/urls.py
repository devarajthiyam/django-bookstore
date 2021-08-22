from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book-list-page'),
    path('<int:pk>', views.book_detail_view, name='book-detail-page'),
]