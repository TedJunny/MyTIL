from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instance_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_instances": num_instance,
        "num_instances_available": num_instance_available,
        "num_authors": num_authors,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
