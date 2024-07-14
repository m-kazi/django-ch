from django.contrib import admin
from .models import CoffeeTypes, CoffeeReview, CoffeeCerts, Store


# ----> Register your models here <----


# inline review box for CoffeeTypes
class CoffeeReviewInline(admin.TabularInline):
    model = CoffeeReview
    extra = 1


class CoffeeTypesAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [CoffeeReviewInline]


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("coffee", "cert_number")


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("coffee_varieties",)


# Register models, custommodel class
admin.site.register(CoffeeTypes, CoffeeTypesAdmin)
admin.site.register(CoffeeCerts, CertificateAdmin)
admin.site.register(Store, StoreAdmin)
