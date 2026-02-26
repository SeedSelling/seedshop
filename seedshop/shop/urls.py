from django.urls import path
from . import views

app_name = 'shop'  # Namespace add to avoid conflicts [web:20]

urlpatterns = [
    path('', views.home, name='home'),
    path('seeds/', views.category_list, name='category_list'),
    path('seeds/<str:category>/', views.seed_by_category, name='seed_by_category'),
    path('search/', views.seed_search, name='seed_search'),
    path('seeds/search-varieties/', views.seed_search_varieties, name='seed_search_varieties'),
    path('booking/', views.create_booking, name='create_booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('book/<int:seed_id>/', views.book_seed, name='book_seed'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('reports/status/', views.status_report, name='status_report'),
    path('pay/<int:seed_id>/', views.fake_payment, name='pay'),
    path('bookings/', views.booking_list, name='booking_list'),
]
