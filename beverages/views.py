from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Beverages, BeveragesCategories
from .forms import CreateBeveragesForm, EditBeveragesForm, CreateBeverageCategoriesForm, EditBeverageCategoriesForm

# Create your views here.


def beverages_index(request):
    icecekler = Beverages.objects.filter(isActive=1)
    

    return render(request, "beverages/index.html", {"icecekler": icecekler})
    

def beveragesByCategory(request):
    # icecekler = Beverages.objects.filter(categories__title=request, isActive=1)
    icecekler = Beverages.objects.filter(isActive=1)


    return render(request, "beverages/index.html", {"icecekler": icecekler})

def create_beverages(request):
    if request.method == "POST":
        form = CreateBeveragesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages_menu")
    else:
        form = CreateBeveragesForm()

    return render(request, "beverages/create-beverages.html", {"form": form})


def edit_beverages(request, slug):
    beverage = get_object_or_404(Beverages, slug=slug)
    if request.method == "POST":
        form = EditBeveragesForm(request.POST, request.FILES, instance=beverage)
        form.save()
        return redirect("pages_menu")
    else:
        form = EditBeveragesForm(instance=beverage)

    return render(request, "beverages/edit-beverages.html", {"form": form, "slug": slug})


def delete_beverages(request, slug):
    beverage = get_object_or_404(Beverages, slug=slug)
    if request.method == "POST":
        beverage.delete()
        return redirect("pages_menu")
    return render(request, "beverages/delete-beverages.html", {"beverage": beverage})




# kategoriler

def create_beverageCategories(request):
    if request.method == "POST":
        form = CreateBeverageCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages_menu")
    else:
        form = CreateBeverageCategoriesForm()

    return render(request, "beverages/create-beverage-category.html", {"form": form})

def edit_beverageCategories(request, slug):
    category = get_object_or_404(BeveragesCategories, slug=slug)
    if request.method == "POST":
        form = EditBeverageCategoriesForm(request.POST, request.FILES, instance=category)
        form.save()
        return redirect("pages_menu")
    else:
        form = EditBeverageCategoriesForm(instance=category)

    return render(request, "beverages/edit-beverage-categories.html", {"form": form, "slug": slug})

def delete_beverageCategories(request, slug):
    category = get_object_or_404(BeveragesCategories, slug=slug)
    if request.method == "POST":
        category.delete()
        return redirect("pages_menu")
    return render(request, "beverages/delete-beverage-category.html", {"category": category})