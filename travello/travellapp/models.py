from django.db import models

# Create your models here.
class Destination:
    id: int
    name: str
    des: str
    img: str
    price: int
    offer: bool