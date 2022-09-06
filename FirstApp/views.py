from django.shortcuts import render
from FirstApp.models import Product
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, "FirstApp/homepage.html")


def contact(request):
    return render(request, 'FirstApp/contactpage.html')


def about(request):
    return render(request, "FirstApp/aboutpage.html")


def add_page(request):
    return render(request, "FirstApp/Addpage.html")


def add_product(request):
    item_id = request.POST['itemid']
    item_name = request.POST['ItemName']
    item_price = request.POST['price']
    item_availability = True
    query = Product(itemid= item_id, ItemName = item_name, Price = item_price, Availability = item_availability)
    query.save()
    return HttpResponseRedirect(reverse('display'))


def get_data(request):
    query = Product.objects.all()
    context = { "query" : query}
    return render(request, 'FirstApp/display.html', context)


def update_data(request, id):
    # payload = request.data
    query = Product.objects.get(id=id)
    context = {"query" : query}
    return render(request, 'FirstApp/update.html', context)


def record_update(request, id):
    item_id = request.POST['itemid']
    item_name = request.POST['ItemName']
    item_price = request.POST['Price']
    query = Product.objects.get(id=id)
    query.itemid = item_id
    query.ItemName = item_name
    query.Price = item_price
    query.save()
    return HttpResponseRedirect(reverse('display'))


def delete_product(request, _id):
    query = Product.objects.get(id=_id)
    query.delete()
    return HttpResponseRedirect(reverse('display'))

