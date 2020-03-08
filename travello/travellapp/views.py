from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Dhaka"
    dest1.des = "Dhaka is a capital of Bangladesh"
    dest1.price = 1200
    dest1.img = "destination_1.jpg"
    dest1.offer = True

    dest2 = Destination()
    dest2.name = "Barisal"
    dest2.des = "Barisal is a beautiful city"
    dest2.price = 1000
    dest2.img = "destination_2.jpg"
    dest2.offer = False

    dest3 = Destination()
    dest3.name = "Khulna"
    dest3.des = "Khulna city has a nice bridge that is call Rupsha bridge"
    dest3.price = 900
    dest3.img = "destination_3.jpg"
    dest3.offer = False
    
    dest = [dest1, dest2, dest3]

    return render(request, 'index.html', {"dests": dest})
