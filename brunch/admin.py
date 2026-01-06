from django.contrib import admin

from .models import Brunch, BrunchCategories


@admin.register(Brunch)
class BeveragesAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "isActive", "isHome", "image", "category_list",)
    list_display_links = ("title", "slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("isActive", "isHome",)
    list_editable = ("isActive", "isHome",)
    search_fields = ("title", "description",)

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html
    

@admin.register(BrunchCategories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}