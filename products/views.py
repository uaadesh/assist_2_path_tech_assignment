from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    task = ""
    all_products = product.objects.all()
    if request.method == "POST":
        if "search" in request.POST:
            name = request.POST['searchinput']
            print(name)
            all_products = product.objects.filter(Name = name)

        elif "add" in request.POST:
            Name = request.POST['AddNewName']
            price = request.POST['AddNewPrice']
            quantity = request.POST['AddNewQuantity']
            newProduct = product(Name=Name, price=price, quantity=quantity)
            newProduct.save()
            task = "add"

        elif "edit" in request.POST:
            product_id = request.POST['pid']
            editname = request.POST['EditName']
            editprice = request.POST['EditPrice']
            editquantity = request.POST['EditQuantity']
            prod = product.objects.filter(P_id=product_id)[0]
            prod.Name = editname
            prod.price = editprice
            prod.quantity = editquantity
            prod.save()
            task = "update"

    return render(request, "index.html", {"all_products":all_products, "task":task})