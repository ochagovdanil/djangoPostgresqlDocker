from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_books),
	path('read/<str:pk>', views.get_book_by_id),
	path('add/', views.add_book),
	path('update/<str:pk>', views.update_book_by_id),
	path('delete/<str:pk>', views.delete_book_by_id),
]