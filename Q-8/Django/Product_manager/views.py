from django.shortcuts import render
from Product_manager.models import *
# Create your views here.

def home(request):
    context = {}
    if request.method == "POST":
        Product.objects.create(
            Product_id=request.POST["fname"],
            product_name=request.POST["lname"]
        )
        context["msg"] = "value updated successfully"
    return render(request, "home.html", context)


def records(request):
    context = {}
    all_records = Product.objects.all()
    # print(dict(all_records))
    context["all_records"] = all_records
    return render(request, "records.html", context)
