from django.shortcuts import render
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def show_watchlist(request):
    data_film = MyWatchList.objects.all()
    context = {
    'watchlist' : data_film,
    'nama': 'Annava',
    'id':'2106635493'
    }
    return render(request, "watchlist.html", context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
