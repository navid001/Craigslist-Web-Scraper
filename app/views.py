from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request,'index.html')

def new_search(request):
    return render(request,'newsearch.html')

def search(request):
    # url='https://newyork.craigslist.org/search/bbb?query='
    search=request.POST.get('search')
    # final_url=url+search
    # print(final_url)
    search_parameters = {
        'search':search,
    }
    return render(request,'search.html',search_parameters)