from rest_framework import serializers
from rest_framework.fields import DateTimeField


# Authorities to choose from including a test authority
AUTHORITIES = {
    "United Kingdom": {
        "Modern Slavery & Exploitation Helpline": "info@modernslaveryhelpline.org",
        "Crimestoppers": "contactus@crimestoppers-uk.org",
    },
    "Ireland": {
        "An Garda Síochána (HTICU)": "blueblindfold@garda.ie",
        "Department of Justice and Equality (AHTU)": "ahtu_inbox@justice.ie",
    },
}

# CHOICES from AUTHORITIES
AUTHORITY_CHOICES = [
    (authority, authority)
    for country_authorities in AUTHORITIES.values()
    for authority in country_authorities.keys()
]


class ReportSerializer(serializers.Serializer):
    # optional fields
    name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    # Required fields
    location = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date_and_time = serializers.DateTimeField(required=True, format="%Y-%m-%dT%H:%M")
    category = serializers.CharField(required=True)
    authority = serializers.ChoiceField(choices=AUTHORITY_CHOICES, required=True)
