from django.shortcuts import render
from catalog.models import Book, Author, BookInstance


def index(request):

    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instance_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instance,
        "num_instances_available": num_instance_available,
        "num_authors": num_authors,
    }

    return render(request, "index.html", context=context)