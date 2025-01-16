from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

from .serializers import ReportSerializer

# Map each country to the possible authorities + emails
AUTHORITIES = {
    "United Kingdom": {
        "Modern Slavery & Exploitation Helpline": "info@modernslaveryhelpline.org",
        "Crimestoppers": "contactus@crimestoppers-uk.org",
        "Testing Authority": "",  # <--- add a test email
    },
    "Ireland": {
        "An Garda Síochána (HTICU)": "blueblindfold@garda.ie",
        "Department of Justice and Equality (AHTU)": "ahtu_inbox@justice.ie",
        "Testing Authority": "",  # <--- add a test email
    },
}


class ReportCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            name = data.get("name", "")
            email = data.get("email", "")
            location = data["location"]
            description = data["description"]
            date_and_time = data["date_and_time"]
            category = data["category"]
            country = data["country"]
            authority = data["authority"]

            # Find the email address for that (country, authority) combination
            if authority in AUTHORITIES.get(country, {}):
                recipient_email = AUTHORITIES[country][authority]
            else:
                return Response(
                    {"error": "Invalid authority for the chosen country."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Prepare email message
            subject = "New Suspicious Activity Report"
            message = (
                f"A new report has been submitted.\n\n"
                f"Name: {name or 'Not provided'}\n"
                f"Email: {email or 'Not provided'}\n"
                f"Location: {location}\n"
                f"Description: {description}\n"
                f"Date/Time: {date_and_time}\n"
                f"Category: {category}\n"
            )

            # Send email
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,  # The "sender"
                    [recipient_email],  # The "recipient"
                    fail_silently=False,
                )
                return Response(
                    {"message": "Report successfully created and email sent."},
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response(
                    {"error": f"Error sending email: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
