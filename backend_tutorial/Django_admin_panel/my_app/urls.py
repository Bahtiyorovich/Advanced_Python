from django.urls import path
from .views import home, pages

urlpatterns = [
    path('', home, name='home_page'),
    path('page/<str:page>',pages, name='pages'),
]