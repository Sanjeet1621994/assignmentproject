import json
from math import ceil

from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Contact, Order, OrderUpdate


def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def DisplayProducts(request):
    return HttpResponse("params")


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        c = Contact()
        c.name = request.POST['txtname']
        c.phone = request.POST['txtphone']
        c.email = request.POST['txtemail']
        c.query = request.POST['txtquery']
        c.save()
        msg = "your query has been submitted we will contact you shortly in the meantime you can checkout our products"
        return render(request, 'shop/contact.html', {'msg': msg})

    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def productview(request, id):
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == 'POST':
        c = Order()
        c.name = request.POST['username']
        c.email = request.POST['useremail']
        c.address = request.POST['useraddress1'] + ' ' + request.POST['useraddress2']
        c.city = request.POST['usercity']
        c.zipcode = request.POST['userzip']
        c.phone = request.POST['userphone']
        c.items_json = request.POST['itemsJson']
        c.state = request.POST['userstate']
        c.save()
        update = OrderUpdate(order_id=c.order_id, update_desc="The order has been placed")
        update.save()
        thank= True
        return render(request, 'shop/checkout.html',{'thank':thank,'id':c.order_id})
    return render(request, 'shop/checkout.html')


def search(request):
    return render(request, 'shop/search.html')










