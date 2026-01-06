from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from brunch.models import Brunch, BrunchCategories
from .forms import CreateBrunchCategoriesForm, EditBrunchCategoriesForm, CreateBrunchForm, EditBrunchForm
from django.contrib.auth.decorators import login_required


def brunch_index(request):
    brunches = Brunch.objects.filter(isActive=1)
    

    return render(request, "brunch/index.html", {"brunches": brunches})

@login_required()
def create_brunch(request):
    if request.method == "POST":
        form = CreateBrunchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages_menu")
    else:
        form = CreateBrunchForm()

    return render(request, "brunch/create-brunch.html", {"form": form})

@login_required()
def edit_brunch(request, slug):
    brunch = get_object_or_404(Brunch, slug=slug)
    if request.method == "POST":
        form = EditBrunchForm(request.POST, request.FILES, instance=brunch)
        form.save()
        return redirect("pages_menu")
    else:
        form = EditBrunchForm(instance=brunch)

    return render(request, "brunch/edit-brunch.html", {"form": form, "slug": slug})


@login_required()
def delete_brunch(request, slug):
    brunch = get_object_or_404(Brunch, slug=slug)
    if request.method == "POST":
        brunch.delete()
        return redirect("pages_menu")
    return render(request, "brunch/delete-brunch.html", {"brunch": brunch})



# kategoriler

@login_required()
def create_brunchCategories(request):
    if request.method == "POST":
        form = CreateBrunchCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages_menu")
    else:
        form = CreateBrunchCategoriesForm()

    return render(request, "brunch/create-brunch-category.html", {"form": form})

@login_required()
def edit_brunchCategories(request, slug):
    category = get_object_or_404(BrunchCategories, slug=slug)
    if request.method == "POST":
        form = EditBrunchCategoriesForm(request.POST, request.FILES, instance=category)
        form.save()
        return redirect("pages_menu")
    else:
        form = EditBrunchCategoriesForm(instance=category)

    return render(request, "brunch/edit-brunch-categories.html", {"form": form, "slug": slug})


@login_required()
def delete_brunchCategories(request, slug):
    category = get_object_or_404(BrunchCategories, slug=slug)
    if request.method == "POST":
        category.delete()
        return redirect("pages_menu")
    return render(request, "brunch/delete-brunch-category.html", {"category": category})