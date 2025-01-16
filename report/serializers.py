from rest_framework import serializers


COUNTRY_CHOICES = [
    ("United Kingdom", "United Kingdom"),
    ("Ireland", "Ireland"),
]

# Authorities to choose from including a test authority
AUTHORITY_CHOICES = [
    (
        "Modern Slavery & Exploitation Helpline",
        "Modern Slavery & Exploitation Helpline",
    ),
    ("Crimestoppers", "Crimestoppers"),
    ("An Garda Síochána (HTICU)", "An Garda Síochána (HTICU)"),
    (
        "Department of Justice and Equality (AHTU)",
        "Department of Justice and Equality (AHTU)",
    ),
    ("Testing Authority", "Testing Authority"),  # For testing
]


class ReportSerializer(serializers.ModelSerializer):
    # optional fields
    name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    # Required fields
    location = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date_and_time = serializers.CharField(required=True)
    category = serializers.CharField(required=True)

    country = serializers.ChoiceField(choices=COUNTRY_CHOICES, required=True)
    authority = serializers.ChoiceField(choices=AUTHORITY_CHOICES, required=True)
