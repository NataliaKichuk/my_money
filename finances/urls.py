from django.urls import path
from finances import views
urlpatterns = [
	path('', views.home_view, name='home'),
	path('finances/', views.record_list, name='record_list'),
	path('finances/income_create/', views.income_create, name='income_create'),
	path('finances/expense_create/', views.expense_create, name='expense_create'),
	path('finances/<int:pk>/edit/', views.record_edit, name='record_edit'),
	path('finances/<int:pk>/delete/', views.record_delete, name='record_delete'),
	path('finances/categories/', views.category_list, name='categories_list'),
	path('finances/categories/create/', views.category_create, name='category_create'),
	path('finances/categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
	path('finances/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

]