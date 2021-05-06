from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetails.as_view()),
    path('users/', views.AuthorList.as_view()),
    path('users/<int:pk>/', views.AuthorDetails.as_view()),
]


