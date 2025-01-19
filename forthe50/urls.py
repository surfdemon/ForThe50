from django.urls import path
from .views import about, contact, index, team, statistics, ReportView, knowledge


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("meet-team/", team, name="meet_team"),
    path("statistics/", statistics, name="statistics"),
    path("report/", ReportView.as_view(), name="report"),
    path("knowledge/", knowledge, name="knowledge"),
]
