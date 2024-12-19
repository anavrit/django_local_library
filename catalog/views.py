from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    non_fiction = ["History", "Reality"]
    num_nonfiction_books = Genre.objects.filter(name__in=non_fiction).count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_nonfiction_books': num_nonfiction_books,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'chinese_books'
    template_name = 'books/book_list.html'
    def get_queryset(self):
        return Book.objects.filter(language__name__iexact='Chinese')

class BookDetailView(generic.DetailView):
    model = Book

