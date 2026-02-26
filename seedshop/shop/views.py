from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Seed, Booking

def home(request):
    return render(request, 'shop/home.html', {'title': 'Seed Booking System'})

def seeds_redirect(request):
    return redirect('seed_search')

def category_list(request):
    categories = Seed.objects.values_list('category', flat=True).distinct()
    return render(request, 'shop/category_list.html', {'categories': categories})

def seed_by_category(request, category):
    seeds = Seed.objects.filter(category=category).order_by('name')
    return render(request, 'shop/seed_by_category.html', {'category': category, 'seeds': seeds})

def seed_search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    seeds = Seed.objects.all()
    
    if query:
        seeds = seeds.filter(name__icontains=query)
    
    if category:  # ← YE LINE MISSING HOGI
        seeds = seeds.filter(category__icontains=category)
    
    context = {
        'seeds': seeds,
        'query': query,
        'category': category,
    }
    return render(request, 'shop/search.html', context)

#def seed_search(request):
    query = request.GET.get('q')
    results = Seed.objects.all()
    if query:
        results = results.filter(Q(name__icontains=query) | Q(category__icontains=query))
    return render(request, 'shop/search.html', {'seeds': results, 'query': query})

def seed_search_varieties(request):
    query = request.GET.get('q')
    results = Seed.objects.all()
    if query:
        results = results.filter(name__icontains=query)  # variety field नहीं है तो name use करो
    return render(request, 'shop/search.html', {'seeds': results, 'query': query})  # same template


def create_booking(request):
    if request.method == 'POST':
        farmer_name = request.POST.get('farmer_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        seed_id = request.POST.get('seed_id')
        quantity = request.POST.get('quantity')
        seed = get_object_or_404(Seed, id=seed_id)
        Booking.objects.create(
            farmer_name=farmer_name, phone=phone, address=address,
            seed=seed, quantity=int(quantity)
        )
        return redirect('home')
    seeds = Seed.objects.all().order_by('category', 'name')
    return render(request, 'shop/booking_form.html', {'seeds': seeds})

def booking_list(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'shop/booking_list.html', {'bookings': bookings})

@login_required
def manage_bookings(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_status = request.POST.get('status')
        if booking_id and new_status:
            booking = get_object_or_404(Booking, id=booking_id)
            booking.status = new_status
            booking.save()
        return redirect('manage_bookings')
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'manage_bookings.html', {'bookings': bookings})

def my_bookings(request):
    bookings = []
    phone = request.POST.get('phone', '') if request.method == 'POST' else ''
    if phone:
        bookings = Booking.objects.filter(phone=phone).order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings, 'phone': phone})

def status_report(request):
    status = request.GET.get('status', '')
    bookings = Booking.objects.all().order_by('-booking_date')
    if status:
        bookings = bookings.filter(status=status)
    STATUS_CHOICES = ['', 'Pending', 'Confirmed', 'Delivered', 'Cancelled']
    return render(request, 'shop/status_report.html', {
        'bookings': bookings, 'status': status, 'STATUS_CHOICES': STATUS_CHOICES
    })

def book_seed(request, seed_id):
    seed = get_object_or_404(Seed, id=seed_id)
    return render(request, 'shop/book.html', {'seed': seed})

from django.shortcuts import get_object_or_404
from .models import Seed

def fake_payment(request, seed_id):
    seed = get_object_or_404(Seed, id=seed_id)
    return render(request, 'shop/fake_payment.html', {'seed': seed})

def bookings(request):
    return render(request, 'shop/bookings.html', {'bookings': []})

def booking_list(request):
    return render(request, 'shop/bookings.html')




