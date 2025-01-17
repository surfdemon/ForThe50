from django.urls import path
from .views import index, contact, statistics


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('statistics/', statistics, name='statistics'),
]
