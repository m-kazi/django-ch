from django.shortcuts import render
from .models import CoffeeTypes, Store
from django.shortcuts import get_object_or_404
from .forms import CoffeeTypesForm


# Create your views here.
def all_coffee(request):
    coffees = CoffeeTypes.objects.all()
    return render(request, "peets/all_coffee.html", {"coffees": coffees})


def coffee_detail(request, coffee_id):
    coffee = get_object_or_404(CoffeeTypes, pk=coffee_id)
    return render(request, "peets/coffee_detail.html", {"coffee": coffee})


# for coffee_stores.html form
def coffee_stores_view(request):
    stores = None
    # step-1 : form filling & sending
    if request.method == "POST":
        form = CoffeeTypesForm(request.POST)
        # checking form validation & clened the data
        if form.is_valid():
            coffee_types = form.cleaned_data["coffee_types"]
            stores = Store.objects.filter(coffee_varieties=coffee_types)
    else:
        # step-2 : to send the form to user to fill
        form = CoffeeTypesForm()
    return render(request, "peets/coffee_stores.html", {"stores": stores, "form": form})
