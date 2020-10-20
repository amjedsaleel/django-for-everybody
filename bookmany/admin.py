from django.contrib import admin

from .models import Authored, Author, Book

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Authored)
