from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'itemdex/index.html', context)
