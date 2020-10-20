from django.contrib import admin

from .models import Person, Membership, Course

# Register your models here.

admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Course)

