from django.shortcuts import render
from django.http import HttpResponse
from shopApp.models import Product, Contacts

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)

    my_context = {
        'user' : 'Alan',
        'message' : '¡Lárgate!',
        'special_offers' : special_offers,
        'product_list' : product_list,
        'special_offers_2' : [
        {
            'name' : 'Fundas de celular',
            'cost' : 50.00,
            'img'  : 'shopApp/img/funda.jpg'
        },
        {
            'name' : 'Mouse Gamer',
            'cost' : 400.00,
            'img'  : 'shopApp/img/mouse.jpg'
        },
        {
            'name' : 'Teclado Mecánico',
            'cost' : 600.00,
            'img'  : 'shopApp/img/teclado.jpg'
        },
        {
            'name' : 'Llavero de Yoimiya Genshin Impact',
            'cost' : 100.00,
            'img'  : 'shopApp/img/llavero.jpg'
        },
        {
            'name' : 'Mochila Anti-Robo',
            'cost' : 500.00,
            'img'  : 'shopApp/img/mochila.jpg'
        },
        {
            'name' : 'Peluche de Amiya',
            'cost' : 500.00,
            'img'  : 'shopApp/img/amiya.jpg'
        },
        ],
    }

    return render(request, 'shopApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django")

def about(request):
    active_contacts = Contacts.objects.filter(contact_active=True)  #Filtra los contactos activos
    context = {
        'active_contacts': active_contacts  #Pasa los contactos activos al contexto
    }
    return render(request, 'shopApp/about.html', context=context)