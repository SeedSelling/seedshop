from django.contrib import admin
from .models import Seed, Booking, SeedVariety


class SeedVarietyInline(admin.TabularInline):   # ya StackedInline
    model = SeedVariety
    extra = 1   # ek empty row extra dikhane ke लिए


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']  # Subcategory hata diya
    list_filter = ['category']
    search_fields = ['name']
    fields = ['name', 'category', 'price', 'stock', 'description']  # Subcategory exclude


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['farmer_name', 'seed', 'quantity', 'status', 'booking_date']

# Register your models here.
