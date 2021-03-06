from datetime import date
import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):

    """Genre Model Definition"""

    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    def __str__(self):
        return self.name


class Language(models.Model):

    """Language Model Definition"""

    name = models.CharField(
        max_length=200,
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    """Book Model Definition"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=300, help_text="Enter a brief description of the book"
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey("language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def display_genre(self):

        """Create A string for the Genre. This is required to display genre in Admin"""

        return ", ".join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = "Genre"

    def get_absolute_url(self):

        """Returns the url to access a detail record for this book."""

        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):

    """Book Instance Model Definition"""

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library",
    )
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book Availability",
    )
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f"{self.id} ({self.book.title})"

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


class Author(models.Model):

    """Author Model Definition"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
