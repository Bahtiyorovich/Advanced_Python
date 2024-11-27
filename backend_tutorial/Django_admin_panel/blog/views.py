from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    htm = """
        <h1>My Blog App</h1>
    """
    return HttpResponse(htm)

