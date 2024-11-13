from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Advertisement
from django.contrib.auth.decorators import login_required

@login_required
def create_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        location = request.POST['location']
        Listing.objects.create(title=title, description=description, price=price, location=location, posted_by=request.user)
        return redirect('view_listings')
    return render(request, 'listings/create_listing.html')

def view_listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/view_listings.html', {'listings': listings})

def view_listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/view_listing_detail.html', {'listing': listing})

def advertisements(request):
    active_ads = Advertisement.objects.filter(is_active=True)
    return render(request, 'listings/advertisements.html', {'advertisements'})