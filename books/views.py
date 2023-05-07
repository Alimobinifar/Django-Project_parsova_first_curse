from django.shortcuts import render
from books.models import *


def home_page(request):
    qs = Book.objects.all()
    return render(request, 'home.html/',context={"books":qs})