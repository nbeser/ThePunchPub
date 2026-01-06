from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from beverages.models import Beverages, BeveragesCategories
from brunch.models import Brunch, BrunchCategories
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Slider
from .forms import CreateSliderForm, EditSliderForm



def pages_index(request):
    return render(request, "pages/index.html")


def pages_menu(request):
    beverages_categories = BeveragesCategories.objects.all()
    # beverages_categories = get_list_or_404(BeveragesCategories)
    brunch_categories = BrunchCategories.objects.all()
    # brunch_categories = get_list_or_404(BrunchCategories)
    sliders = Slider.objects.filter(is_active=True)

    return render(request, "pages/menu.html", {
        "beverages_categories": beverages_categories,
        "brunch_categories": brunch_categories,
        "sliders": sliders
    })

def products_by_category(request, slug):
    beverages_categories = BeveragesCategories.objects.all()
    brunch_categories = BrunchCategories.objects.all()

    if Beverages.objects.filter(categories__slug=slug, isActive=1).exists():
        obje = Beverages.objects.filter(categories__slug=slug, isActive=1)
        paginator = Paginator(obje, 5)
        page = request.GET.get("page", 1)
        page_obj = paginator.page(page)

        return render(request, "pages/products.html", {
            "products": obje,
            "obje_type": "beverages",
            "beverages_categories": beverages_categories,
            "brunch_categories": brunch_categories,
            "chosenCategory": slug,
            "page_obj": page_obj
            })
    else:
        obje = Brunch.objects.filter(categories__slug=slug, isActive=1)
        paginator = Paginator(obje, 5)
        page = request.GET.get("page", 1)
        page_obj = paginator.page(page)
        return render(request, "pages/products.html", {
            "products": obje,
            "obje_type": "brunch",
            "beverages_categories": beverages_categories,
            "brunch_categories": brunch_categories,
            "chosenCategory": slug,
            "page_obj": page_obj
            })


@login_required()
def user_index(request, username):
    beverages_categories = BeveragesCategories.objects.all()
    brunch_categories = BrunchCategories.objects.all()

    beverages = Beverages.objects.all()
    brunch = Brunch.objects.all()

    slider = Slider.objects.all()

    return render(request, "pages/user_index.html", {
        "username": username,
        "brunch_categories": brunch_categories,
        "beverages_categories": beverages_categories,
        "beverages": beverages,
        "brunch": brunch,
        "slider": slider,
    })


@login_required()
def create_slider(request):
    if request.method == "POST":
        form = CreateSliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pages_menu")
    else:
        form = CreateSliderForm()

    return render(request, "pages/create-slider.html", {"form": form})



def edit_slider(request, id):
    slide = get_object_or_404(Slider, id=id)
    if request.method == "POST":
        form = EditSliderForm(request.POST, request.FILES, instance=slide)
        form.save()
        return redirect("pages_menu")
    else:
        form = EditSliderForm(instance=slide)

    return render(request, "pages/edit-slider.html", {"form": form, "id": id})

@login_required()
def delete_slider(request, id):
    slide = get_object_or_404(Slider, id=id)
    if request.method == "POST":
        slide.delete()
        return redirect("pages_menu")
    return render(request, "pages/delete-slider.html", {"slide": slide})