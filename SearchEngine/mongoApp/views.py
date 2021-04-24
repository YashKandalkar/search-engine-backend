from django.shortcuts import render
from .models import displaySearch

# Create your views here.

def mongoView(request):
    return render(
        request,
        'mongoTemplate.html',
        {
            'displaySearch' : displaySearch("string"),
        }
    )