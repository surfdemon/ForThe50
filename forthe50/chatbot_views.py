from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random
from difflib import SequenceMatcher


def select_response(responses, temperature=0.7):
    if temperature < 0.1:
        return responses[0]
    weights = [((1 - temperature) + random.random() * temperature) for _ in responses]
    total_weight = sum(weights)
    probabilities = [w / total_weight for w in weights]
    return random.choices(responses, weights=probabilities, k=1)[0]


def is_partial_match(keyword, message, threshold=0.6):
    return SequenceMatcher(None, keyword, message).ratio() > threshold


themes = {
    "greeting": {
        "keywords": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "what's up",
            "howdy",
            "hiya",
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What's on your mind?",
            "Hey! How can I help you?",
            "Good to see you! How can I assist?",
            "Hi! What would you like to talk about today?",
            "Hello! Feel free to ask me anything.",
        ],
    },
    "human_trafficking": {
        "keywords": [
            "human trafficking",
            "modern slavery",
            "trafficking",
            "forced labor",
            "child exploitation",
            "labor exploitation",
            "exploitation",
            "sex trafficking",
            "child trafficking",
            "sexual exploitation",
            "bonded labor",
            "slavery",
            "forced work",
            "coerced labor",
            "labor abuse",
            "organ trafficking",
            "organ harvesting",
            "illegal work",
            "human trade",
            "victim of trafficking",
            "victims of slavery",
            "domestic servitude",
            "forced begging",
            "forced prostitution",
            "trafficking of minors",
            "exploitation of children",
            "modern forced labor",
            "trafficked individuals",
            "exploited workers",
            "undocumented labor",
            "illegal exploitation",
            "labor trafficking",
            "harvested organs",
            "work abuse",
            "exploited children",
            "labor violations",
            "abuse of workers",
            "forced movement",
            "smuggling of people",
            "human exploitation",
            "trafficking victims",
            "trafficked workers",
            "migrant exploitation",
            "sex workers exploitation",
        ],
        "responses": [
            "Human trafficking is a serious issue. Please contact authorities or a helpline for assistance.",
            "If you suspect trafficking, report it immediately through our report page: /report/.",
            "Modern slavery is a violation of human rights. Learn more about it on our statistics page: /statistics/.",
            "If someone you know is being trafficked, report it immediately to the relevant authorities or through our contact page: /contact/.",
            "Human trafficking victims often require urgent support. Find resources here: /contact/.",
            "To report suspicious activity related to trafficking or forced labor, use our report form here: /report/.",
            "Trafficking affects millions globally. Learn about how you can make a difference here: /statistics/.",
            "If you believe someone is being exploited, contact local authorities or visit our contact page for resources: /contact/.",
            "Labor trafficking and exploitation are illegal. Report concerns through our report page: /report/.",
            "Organ trafficking is a severe crime. If you suspect it, contact authorities or visit /contact/.",
            "Sex trafficking is a global issue. Learn more about signs and reporting on our statistics page: /statistics/.",
            "Exploitation in any form is a violation of human rights. Take action by reporting it here: /report/.",
            "If you're unsure how to help a trafficking victim, start by visiting our contact page for guidance: /contact/.",
            "The first step to stopping trafficking is awareness. Visit /statistics/ to learn more.",
            "For resources related to labor trafficking, visit our contact page here: /contact/.",
            "Trafficking victims often face physical and emotional abuse. Report any suspicions immediately here: /report/.",
            "Child exploitation is a grave concern. Learn about signs and prevention on our statistics page: /statistics/.",
            "Forced labor and bonded labor destroy lives. If you see signs, take action by reporting: /report/.",
            "Organ harvesting and illegal trafficking are major crimes. Help stop them by reporting suspicious activities: /report/.",
            "To support trafficking victims, connect with local organizations. Start by visiting /contact/.",
            "Trafficking often targets vulnerable individuals. Learn how to recognize and respond here: /statistics/.",
            "Trafficking isn't always obvious. Find out what signs to look for and how to act: /statistics/.",
            "If you're in the UK, contact the Modern Slavery Helpline at +44 800 0121 700 for assistance.",
            "In Ireland, reach out to An Garda Síochána at blueblindfold@garda.ie to report concerns.",
            "Human trafficking can occur in many industries. Learn about risks and responses on our report page: /report/.",
            "Sexual exploitation is a common form of trafficking. If you suspect it, report it here: /report/.",
            "Trafficking is a hidden crime. Raise awareness and act by visiting /statistics/.",
        ],
    },
    "mental_health": {
        "keywords": [
            "mental health",
            "depression",
            "anxiety",
            "stress",
            "worried",
            "panic attack",
            "overwhelmed",
            "mental illness",
            "feeling down",
            "feeling sad",
            "burnout",
            "emotional distress",
            "psychological issues",
            "mental wellbeing",
            "self-care",
            "therapy",
            "counseling",
            "need support",
            "lonely",
            "feeling isolated",
            "trouble coping",
            "trauma",
            "mental support",
            "emotional support",
            "feeling hopeless",
        ],
        "responses": [
            "It's important to care for your mental health. Reach out to someone you trust or a professional.",
            "If you're feeling overwhelmed, here are resources that might help: /contact/.",
            "You are not alone. Consider talking to a mental health professional or visiting our contact page: /contact/.",
            "Feeling stressed? It might help to take small steps or reach out for support. Resources here: /contact/.",
            "Mental health is just as important as physical health. Find resources and support here: /contact/.",
            "If you're experiencing anxiety or depression, seeking help is a sign of strength. Learn more: /contact/.",
            "Taking care of yourself is essential. Explore resources for mental wellbeing here: /contact/.",
            "If you're struggling, remember there are people who care and can help. Visit: /contact/.",
            "For immediate support, consider reaching out to a mental health hotline or a local professional.",
        ],
    },
    "contact_support": {
        "keywords": [
            "contact",
            "who can i contact",
            "phone number",
            "helpline",
            "get in touch",
            "reach someone",
            "support hotline",
            "emergency contact",
            "help center",
            "hotline number",
            "support number",
            "email support",
            "how to contact",
            "contact details",
            "contact info",
            "support line",
            "need help",
            "ask for help",
            "who do i call",
            "reach out",
            "help contact",
        ],
        "responses": [
            "You can contact the Modern Slavery Helpline (UK) at +44 800 0121 700.",
            "For assistance in Ireland, contact An Garda Síochána (HTICU) at blueblindfold@garda.ie.",
            "Visit our contact page for more information: /contact/.",
            "If you need urgent support, reach out to the Modern Slavery Helpline (UK) at +44 800 0121 700.",
            "For support in Ireland, contact the Department of Justice at ahtu_inbox@justice.ie.",
            "Find more contact details on our support page: /contact/.",
        ],
    },
    "report_crime": {
        "keywords": [
            "report",
            "how can i report",
            "crime",
            "tip",
            "report crime",
            "submit report",
            "suspicious activity",
            "human trafficking report",
            "how to report",
            "file a report",
            "report human trafficking",
            "report slavery",
            "report exploitation",
            "where to report",
            "crime reporting",
            "report abuse",
            "forced labor report",
        ],
        "responses": [
            # UK Responses
            "If you are in the UK, you can report to the Modern Slavery Helpline by calling +44 800 0121 700 or visiting our report page here: /report/.",
            "In the UK, you can also report anonymously to Crimestoppers by emailing contactus@crimestoppers-uk.org. For more options, visit: /report/.",
            "To report a crime in the UK, use our report form: /report/. You can also call the Modern Slavery Helpline directly at +44 800 0121 700.",
            "If you suspect human trafficking or forced labor in the UK, report it to the Modern Slavery Helpline or submit your concerns via /report/.",
            # Ireland Responses
            "For reports in Ireland, contact An Garda Síochána (HTICU) at blueblindfold@garda.ie or visit our report page for assistance: /report/.",
            "If you're in Ireland, you can email the Department of Justice at ahtu_inbox@justice.ie to report human trafficking. More details are available at: /report/.",
            "To report exploitation or suspicious activities in Ireland, visit our report page: /report/. You can also reach out to An Garda Síochána via blueblindfold@garda.ie.",
            # General Guidance
            "Reporting suspicious activities can save lives. Please visit our detailed report page here: /report/.",
            "If you're unsure how to report, start by visiting /report/ for detailed instructions and contact information.",
            "Whether you're in the UK or Ireland, you can use our report page to share your concerns: /report/.",
            "All reports are confidential and will be handled by the appropriate authorities. Start your report here: /report/.",
            "If you know someone at risk, act now. Use our report page to provide details: /report/.",
        ],
    },
    "help_someone": {
        "keywords": [
            "help someone",
            "support someone",
            "how can i help",
            "assist someone",
            "help a friend",
            "help a victim",
            "how do i help",
            "what can i do",
            "how to assist",
            "offer help",
            "help a trafficked person",
            "how can i help a victim",
            "help someone in need",
            "how to support",
            "helping others",
            "how to protect someone",
            "assist trafficking victim",
        ],
        "responses": [
            # General Guidance
            "If you want to help someone, the best place to start is our contact page: /contact/.",
            "You can provide support by reporting suspicious activity through our report page: /report/.",
            "Helping someone starts with awareness. Visit our statistics page to learn more: /statistics/.",
            "If someone you know may be a victim, encourage them to seek help. Resources are available here: /contact/.",
            "Support someone in need by reporting any concerns you have on our report page: /report/.",
            # UK-Specific Responses
            "In the UK, you can call the Modern Slavery Helpline at +44 800 0121 700 to report or support someone.",
            "To help someone in the UK, you can contact Crimestoppers anonymously at contactus@crimestoppers-uk.org.",
            # Ireland-Specific Responses
            "If you're in Ireland, you can assist by contacting An Garda Síochána at blueblindfold@garda.ie.",
            "In Ireland, reach out to the Department of Justice at ahtu_inbox@justice.ie for guidance.",
            # Additional Resources
            "Helping someone can make a difference. Visit our contact page for resources: /contact/.",
            "To support someone in need, report any suspicious activity here: /report/.",
            "If you're not sure where to start, learn about trafficking and resources here: /statistics/.",
            "Acting quickly can save lives. Report or seek guidance through our support page: /contact/.",
        ],
    },
}


@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").lower()
            bot_response = (
                "I'm sorry, I didn't quite catch that. Could you please tell me more?"
            )

            # Check if user message contains a specific country
            country = None
            if "ireland" in user_message:
                country = "Ireland"
            elif "uk" in user_message or "united kingdom" in user_message:
                country = "United Kingdom"

            # Loop through themes and keywords to find a match
            for theme, details in themes.items():
                for keyword in details["keywords"]:
                    if is_partial_match(keyword, user_message):
                        if theme == "report_crime" and country:
                            # Provide specific contact details based on country
                            if country == "Ireland":
                                bot_response = (
                                    "In Ireland, you can email the Department of Justice at ahtu_inbox@justice.ie "
                                    "or contact An Garda Síochána at blueblindfold@garda.ie. More details here: /report/."
                                )
                            elif country == "United Kingdom":
                                bot_response = (
                                    "In the UK, contact the Modern Slavery Helpline at +44 800 0121 700 "
                                    "or Crimestoppers at contactus@crimestoppers-uk.org. Report here: /report/."
                                )
                        elif theme == "report_crime" and not country:
                            #
                            bot_response = "Could you please specify your location (UK or Ireland) so I can provide accurate details?"
                        else:
                            bot_response = random.choice(details["responses"])
                        return JsonResponse({"response": bot_response})

            # If no theme match, provide a general response
            return JsonResponse({"response": bot_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
