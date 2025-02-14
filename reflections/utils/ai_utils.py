import google.generativeai as genai
from django.conf import settings

# Ensure API key is loaded from settings
genai.configure(api_key=settings.GOOGLE_AI_API_KEY)

def generate_reflection_summary(content: str) -> str:
    """Uses Gemini AI to summarize a reflection in 2-3 key points."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Summarize this reflection in 2-3 key points: {content}")

        if not response.candidates:
            return "AI could not generate a summary."

        return response.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        return f"AI processing failed: {str(e)}"
    
def analyze_reflection_with_insights(content: str):
    """Uses Gemini AI to summarize reflections and analyze sentiment."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Summarize this reflection in 2-3 key points and determine if the tone is Positive, Neutral, or Negative:\n{content}"
        )

        if not response.candidates:
            return "AI could not generate insights.", "Neutral"

        response_text = response.candidates[0].content.parts[0].text.strip()
        summary, sentiment = response_text.split("\n")[:2]  # Extract summary & sentiment

        return summary, sentiment

    except Exception as e:
        return f"AI processing failed: {str(e)}", "Neutral"