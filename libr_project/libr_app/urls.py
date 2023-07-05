from django.urls import path
from libr_app import views

urlpatterns=[
    path('',views.BookCreateList.as_view(),name="book-list"),
    path('<int:pk>',views.BookDetail.as_view(),name="book-detail"),
]
