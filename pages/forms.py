from django import forms

from .models import Slider

class CreateSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ("title", "description", "image", "is_active",)
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "image": "Afiş",
            "is_active": "Aktif mi?"
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(),
        }

        error_messages = {
            "title": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter"
            },
            "description": {
                "required": "Zorunlu alan!"
            },
            "image": {
                "required": "Zorunlu alan!"
            },
            "is_active": {
                "required": "Zorunlu alan!"
            }
        }

class EditSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ("title", "description", "image", "is_active",)
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "image": "Afiş",
            "is_active": "Aktif mi?"
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(),
        }

        error_messages = {
            "title": {
                "required": "Zorunlu alan!",
                "max_length": "Maksimum 50 karakter"
            },
            "description": {
                "required": "Zorunlu alan!"
            },
            "image": {
                "required": "Zorunlu alan!"
            },
            "is_active": {
                "required": "Zorunlu alan!"
            }
        }