from django.urls import path
from src import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('book', views.BookListView.as_view(), name='book-list'),
    path('create', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
    path('register/', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout, name='logout')
]
