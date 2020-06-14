from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages, auth

from src.forms import LoginForm, RegisterForm
from src.models import Book


class Index(TemplateView):
    template_name = 'index.html'


def login_page(request):
    form = LoginForm(request.POST or None)
    print("User Logged in => ", request.user.is_authenticated)
    context = {
        "title": 'Form One',
        "content": 'Welcome to Login page',
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print("User Logged in => ", request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print("User Logged in => ", request.user.is_authenticated)
            context['form'] = LoginForm()
            return redirect('index')
        else:
            print("error in login")
            return redirect('login')
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "title": 'Form One',
        "content": 'Welcome to Registration page',
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect('login')

    return render(request, 'register.html', context)


@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'create.html'
    fields = ('name', 'isbn_number')
    success_url = reverse_lazy('book-list')


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'


@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'update.html'
    context_object_name = 'book'
    fields = ('name', 'isbn_number')

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('book-list')
