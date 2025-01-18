from django.urls import path
from . views import contact, index, team, statistics


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('meet-team/', team, name='meet_team'),
    path('statistics/', statistics, name='statistics'),
]
