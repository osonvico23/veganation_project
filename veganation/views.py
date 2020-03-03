from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'veganation/index.html', context=context_dict)
    
# Create your views here.
