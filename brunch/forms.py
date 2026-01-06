from django import forms

from .models import Brunch, BrunchCategories

class CreateBrunchForm(forms.ModelForm):
    class Meta:
        model = Brunch
        fields = ("title", "description", "price", "image", "categories", "isActive",)
        labels = {
            "title": "Yiyecek Adı",
            "description": "Açıklama",
            "price": "Fiyat",
            "isActive": "Aktif mi?",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "price": forms.Textarea(attrs={"class": "form-control"}),
            "isActive": forms.CheckboxInput(),
            "isHome": forms.CheckboxInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter"
            },
            "description": {
                "required": "Zorunlu alan!"
            }
        }



class EditBrunchForm(forms.ModelForm):
    class Meta:
        model = Brunch
        fields = ("title", "description", "price", "image", "categories", "isActive",)
        labels = {
            "title": "Yiyecek Adı",
            "description": "Açıklama",
            "price": "Fiyat",
            "isActive": "Aktif mi?",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "price": forms.Textarea(attrs={"class": "form-control"}),
            "isActive": forms.CheckboxInput(),
            "isHome": forms.CheckboxInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter"
            },
            "description": {
                "required": "Zorunlu alan!"
            }
        }


class CreateBrunchCategoriesForm(forms.ModelForm):
    class Meta:
        model = BrunchCategories
        fields = ("name",)
        labels = {
            "name": "Kategori Adı",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "name": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter",
            }
        }


class EditBrunchCategoriesForm(forms.ModelForm):
    class Meta:
        model = BrunchCategories
        fields = ("name",)
        labels = {
            "name": "Kategori Adı",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "name": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter",
            }
        }


class UploadForm(forms.Form):
    image = forms.ImageField()