from django import forms

from .models import Beverages, BeveragesCategories

class CreateBeveragesForm(forms.ModelForm):
    class Meta:
        model = Beverages
        fields = ("title", "description", "price", "image", "categories", "isActive",)
        labels = {
            "title": "İçecek Adı",
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



class EditBeveragesForm(forms.ModelForm):
    class Meta:
        model = Beverages
        fields = ("title", "description", "price", "image", "categories", "isActive")
        labels = {
            "title": "İçecek Adı",
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


class CreateBeverageCategoriesForm(forms.ModelForm):
    class Meta:
        model = BeveragesCategories
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


class EditBeverageCategoriesForm(forms.ModelForm):
    class Meta:
        model = BeveragesCategories
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