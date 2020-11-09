from django.shortcuts import render
from .models import ClientErip

def index(request):
#    latest_client = ClientErip.object.order_by('-date_add_card')[:5]
    return render(request, 'articles/list.html')
