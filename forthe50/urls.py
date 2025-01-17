from django.urls import path
from .views import contact, index, team, report

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('report/', report, name='report'),
]
