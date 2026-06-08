import json
import google.generativeai as genai
from flask import current_app


class AIService:

    @staticmethod
    def analyze_transcript(transcript_text):

        genai.configure(
            api_key=current_app.config["GEMINI_API_KEY"]
        )

        model = genai.GenerativeModel(
            "gemini-flash-latest"
        )

        prompt = f"""
Analyze the meeting transcript.

Return ONLY valid JSON.

Required format:

{{
  "summary": [
    {{
      "text": "",
      "citations": [
        {{
          "timestamp": ""
        }}
      ]
    }}
  ],
  "actionItems": [
    {{
      "task": "",
      "assignee": "",
      "citations": [
        {{
          "timestamp": ""
        }}
      ]
    }}
  ],
  "decisions": [
    {{
      "text": "",
      "citations": [
        {{
          "timestamp": ""
        }}
      ]
    }}
  ],
  "followUpSuggestions": [
    {{
      "text": "",
      "citations": [
        {{
          "timestamp": ""
        }}
      ]
    }}
  ]
}}

Rules:

- Use ONLY transcript information.
- Do not invent attendees.
- Do not invent action items.
- Do not invent decisions.
- Every item must contain citations.
- Citations must contain timestamps.

Transcript:

{transcript_text}
"""

        response = model.generate_content(
            prompt
        )

        return json.loads(
            response.text
        )