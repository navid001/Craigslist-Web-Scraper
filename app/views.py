from django.shortcuts import render
from requests.compat import quote_plus
import requests
from . import models
from . import scraper
# Create your views here.
def home(request):
    return render(request,'index.html')

def new_search(request):
    return render(request,'newsearch.html')

def search(request):
    search=request.POST.get('search')
    models.Search.objects.create(search=search)
    quote_url=quote_plus(search)
    link=f"https://losangeles.craigslist.org/search/bbb?query={quote_url}"
    search_results=scraper.scrape(link)
    search_parameters = {
        'search':search,
        'search_results':search_results
    }
    return render(request,'search.html',search_parameters)