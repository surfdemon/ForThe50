from django.urls import path
from .views import contact, index, team, statistics, ReportView
from .chatbot_views import chatbot

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("meet-team/", team, name="meet_team"),
    path("statistics/", statistics, name="statistics"),
    path("report/", ReportView.as_view(), name="report"),
    path("chatbot/", chatbot, name="chatbot"),
]