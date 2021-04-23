from django.shortcuts import render
from .models import res

# Create your views here.

def algoliaView(request):
    return render(
        request,
        'algoliaTemplate.html',
        {
            "res" : res,
        }
    )