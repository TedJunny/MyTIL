from django.contrib import admin
from catalog.models import Genre, Language
from . import models


class BooksInline(admin.TabularInline):
    model = models.Book
    extra = 0
    readonly_fields = (
        "title",
        "author",
        "summary",
        "isbn",
        "genre",
        "language",
    )


class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 0
    readonly_fields = (
        "id",
        "book",
        "imprint",
        "due_back",
        "status",
    )


class AuthorAdmin(admin.ModelAdmin):

    """Author Admin Definition"""

    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")

    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

    inlines = [BooksInline]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """Book Admin Definition"""

    list_display = ("title", "author", "display_genre")

    inlines = [BooksInstanceInline]


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    """Book Instance Admin Definition"""

    list_display = (
        "book",
        "status",
        "borrower",
        "due_back",
        "id",
    )

    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availablity", {"fields": ("status", "due_back", "borrower")}),
    )


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
