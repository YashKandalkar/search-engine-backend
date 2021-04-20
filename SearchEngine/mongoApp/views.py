from django.shortcuts import render
from .models import counter, displayData

# Create your views here.

def mongoView(request):
    return render(
        request,
        'mongoTemplate.html',
        {
            'counterValue' : counter(),
            'displayData' : displayData(),
        }
    )