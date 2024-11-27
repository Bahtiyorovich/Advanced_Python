from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    html ="""
        <h1>Home Page</h1>
        <a href="page/compyuters">Compyuters Page >>> </a><br>
        <a href="page/cars">Cars Page >>> </a><br>
        <a href="page/travel">Travel Page >>> </a>
    """
    return HttpResponse(html)


def pages(request, page):
    if page == 'compyuters':
        html:str = f"""
            <a href="../"><< Home Page</a>
            <h1>Module: {page}</h1>
        """

    elif page == 'cars':
        html:str = f"""
            <a href="../"><< Home Page</a>
            <h1>Module: {page}</h1>
        """

    elif page == 'travel':
        html:str = f"""
        <a href="../"><< Home Page</a>
            <h1>Module: {page}</h1>
        """
    return HttpResponse(html)