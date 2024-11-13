from msilib.schema import Property

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserLoginForm, AddProductForm, EditProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product



# Create your views here.
def home(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'core/home.html', context)


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "core/signup.html", context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("core:home")

    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "core/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required
def new_item(request):
    form = AddProductForm()

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("core:home")

    context = {"form": form}
    return render(request, "core/form.html", context)


@login_required
def edit_item(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)

    form = EditProductForm(instance=product)

    if request.method == "POST":
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    context = {
        "form": form,
        "product": product
    }
    return render(request, "core/form.html", context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "core/detail.html", context)


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == "POST":
        product.delete()
        return redirect("core:home")

    context = {
        "product": product,
    }
    return render(request, "core/delete.html", context)


def search(request):
    query = request.GET.get("query", "")

    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        "query": query,
        "products": products
    }
    return render(request, 'core/search.html', context)


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'core/properties.html', {'properties': properties})


def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'core/property_detail.html', {'property': property})


def buy_property(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'core/buy_property.html', {'property': property})


def confirm_purchase(request, id):
    if request.method == 'POST':
        property = get_object_or_404(Property, id=id)

        # Add logic to mark property as sold (e.g., set property.is_sold = True and save)
        property.is_sold = True
        property.save()

        messages.success(request, "Congratulations! You've successfully purchased the property.")
        return redirect('property_list')
    return redirect('property_detail', id=id)


