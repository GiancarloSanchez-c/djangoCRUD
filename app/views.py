from .form import LoginForm, AuthorForm, BookForm
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Author, Book
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class LoginPageView(FormView):
    template_name = 'views/auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app:home')
    
    
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('app:home'))
        return super(FormView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginPageView, self).form_valid(form)


class AuthorList(ListView):
    model = Author
    template_name = 'views/author/list.html'
    queryset = Author.objects.all()
    context_object_name = 'authors'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"] = "Hola"
        return context

class AuthorCreate(CreateView):
    form_class = AuthorForm
    template_name = 'views/author/forms/create.html'
    success_url = reverse_lazy('app:author/list')

    def form_valid(self, form):
        success(self.request, 'Se creo el autor con éxito')
        return super().form_valid(form)

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'views/author/forms/update.html'
    success_url = reverse_lazy('app:author/list')
    
    def form_valid(self, form):
        success(self.request, 'Se actualizo el autor con éxito')
        return super().form_valid(form)

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'views/author/forms/delete.html'
    success_url = reverse_lazy('app:author/list')

class BookList(ListView):
    model = Book
    template_name = 'views/book/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'

class BookCreate(CreateView):
    form_class = BookForm
    template_name = 'views/book/forms/create.html'
    success_url = reverse_lazy('app:book/list')
    
    def form_valid(self, form):
        success(self.request, 'Se creo el libro con éxito')
        return super().form_valid(form)
    
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'views/book/forms/update.html'
    success_url = reverse_lazy('app:book/list')
    
    def form_valid(self, form):
        success(self.request, 'Se actualizo el libro con exito')
        return super().form_valid(form)


class BookDelete(DeleteView):
    model = Book
    template_name = 'views/book/forms/delete.html'
    success_url = reverse_lazy('app:book/list')
