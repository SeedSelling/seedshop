"""
URL configuration for seedshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # ← 'include' ADD KARO
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # Seeds listing
    path('seeds/', views.category_list, name='category_list'),
    path('seeds/<str:category>/', views.seed_by_category, name='seed_by_category'),

    # Booking
    path('booking/', views.create_booking, name='create_booking'),
    path('bookings/', views.booking_list, name='booking_list'),

    # Manage & My bookings
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),

    # Seed search
    path('reports/status/', views.status_report, name='status_report'),
    path('search/', views.seed_search, name='seed_search'),
    path('seeds/search-varieties/', views.seed_search_varieties, name='seed_search_varieties'),
    path('', include('shop.urls')),  # ← YE FINAL LINE ADD!
    #path('seeds/<str:category>/', views.seed_by_category, name='seed_by_category'),
    #path('seeds/<str:category>/<str:subcategory>/', views.seed_subcategory, name='seed_subcategory'),
]




