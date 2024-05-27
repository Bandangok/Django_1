from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('../data-398-2018-08-30.csv', 'r', encoding='utf8') as f:
        bus_stantions = []
        reader = csv.DictReader(f)
        for row in reader:
            bus_stantions.append(row)
        paginator = Paginator(bus_stantions, 10)
        page_number = int(request.GET.get("page", 1))
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
            }
    return render(request, 'stations/index.html', context)
