from django.views.generic import ListView, DetailView  # new
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    


class BookDetailView(DetailView, LoginRequiredMixin):
    model = Book
    context_object_name = "book"  # new
    template_name = "books/book_detail.html"
    login_url = "account_login"