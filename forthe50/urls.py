from django.urls import path
from . views import contact, index, team, statistics


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('statistics/', statistics, name='statistics'),
]
