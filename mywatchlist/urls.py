# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_watchlist


from mywatchlist.views import show_xml 
from mywatchlist.views import show_json

app_name = 'katalog'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'), 
    path('html/', show_watchlist, name='show_watchlist'), 
    
    path('xml/', show_xml, name = 'show_xml'),
    path('json/', show_json, name='show_json'),
    
]