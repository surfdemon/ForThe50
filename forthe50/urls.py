from django.urls import path
from .views import contact, index, team

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
]
