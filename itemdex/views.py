from django.shortcuts import render
from itemdex.models import Item

def index(request):
    item_list = Item.objects.all().order_by('game_id')
    context = {'item_list': item_list}
    return render(request, 'itemdex/index.html', context)
