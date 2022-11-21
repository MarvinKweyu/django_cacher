from django.shortcuts import render
from ecommerce.models import Book
from django.views.decorators.cache import cache_page


@cache_page(60*15)  # cache page for 15 minutes
def book_list(request):
    books = Book.objects.all()
    return render(request, "ecommerce/book_list.html", {'books': books})
