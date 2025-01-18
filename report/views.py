from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from .serializers import ReportSerializer

AUTHORITIES = {
    "United Kingdom": {
        "Modern Slavery & Exploitation Helpline": "info@modernslaveryhelpline.org",
        "Crimestoppers": "contactus@crimestoppers-uk.org",
        "Testing Authority": settings.TEST_EMAIL,
    },
    "Ireland": {
        "An Garda Síochána (HTICU)": "blueblindfold@garda.ie",
        "Department of Justice and Equality (AHTU)": "ahtu_inbox@justice.ie",
        "Testing Authority": settings.TEST_EMAIL,
    },
}


class ReportView(View):
    def get(self, request):
        return render(request, "report/report.html")

    def post(self, request):
        data = request.POST.dict()
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            recipient_email = AUTHORITIES[validated_data["country"]].get(
                validated_data["authority"]
            )
            if not recipient_email:
                return JsonResponse(
                    {"error": "Invalid authority for the chosen country."}, status=400
                )

            # Send email
            subject = "New Suspicious Activity Report"
            message = (
                f"Name: {validated_data.get('name', 'Not provided')}\n"
                f"Email: {validated_data.get('email', 'Not provided')}\n"
                f"Location: {validated_data['location']}\n"
                f"Description: {validated_data['description']}\n"
                f"Date/Time: {validated_data['date_and_time']}\n"
                f"Category: {validated_data['category']}\n"
            )

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
                return JsonResponse({"message": "Report submitted successfully."})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse(serializer.errors, status=400)
