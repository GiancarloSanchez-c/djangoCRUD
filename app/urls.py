from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AuthorCreate, BookCreate, AuthorList, AuthorUpdate, AuthorDelete, BookList, BookUpdate, BookDelete, HomePageView 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('author/list',   login_required(AuthorList.as_view()), name='author/list'),
    path('author/create', login_required(AuthorCreate.as_view()), name='author/create'),
    path('author/update/<pk>', login_required(AuthorUpdate.as_view()), name='author/update'),
    path('author/delete/<pk>', login_required(AuthorDelete.as_view), name='author/delete'),
    
    path('book/list', login_required(BookList.as_view()), name='book/list'),
    path('book/create', login_required(BookCreate.as_view()), name='book/create'), 
    path('book/update/<pk>', login_required(BookUpdate.as_view()), name='book/update'),
    path('book/delete/<pk>', login_required(BookDelete.as_view()), name='book/delete')
]
