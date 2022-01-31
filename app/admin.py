from django.contrib import admin
from .models import Author, Book

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =['id','name','last_name','country']
    search_fields = ['name','last_name','country']
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =['id','title','date_published']
    search_fields = ['title']