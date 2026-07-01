import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_content(text):

    prompt = f"""
You are an expert website analyst and information architect.

Analyze the webpage objectively.

Return ONLY valid JSON in exactly this format:

{{
  "headline":"",
  "tagline":"",
  "genre":"",
  "service_type":"",
  "overview":"",
  "key_takeaways":[],
  "highlights":[],
  "audience":"",
  "intent":"",
  "cta":[],
  "recommendation":"",
  "interesting_insight":"",
  "confidence":"",
  "content_flag":{{
      "level":"",
      "reason":""
  }}
}}

Rules:

- Headline: Maximum 10 words.
- Genre: Classify into categories such as Technology, Education, Research, Finance, Healthcare, Government, News, Entertainment, Blog, Documentation, E-commerce, Portfolio, etc.
- Service Type: Identify the type of website (SaaS, Marketplace, Documentation, Blog, News Portal, Community, Government Service, Portfolio, etc.).
- Overview: Summarize the page in under 120 words using simple language.
- Key Takeaways: Return 3–5 concise factual bullet points.
- Purpose: Explain why the webpage exists.
- Audience: Identify the intended audience.
- Intent: Choose one of: Inform, Educate, Sell, Persuade, Support, Community.
- CTA: List important calls to action found on the page.
- Recommendation: Suggest the most useful next step for a visitor.
- Content Flag:
  - level: Safe, Sensitive, or Potentially Harmful
  - reason: Explain why that classification was chosen.

Do not invent facts.
If information is unavailable, return an empty string or an empty list.

Website Content:

{text}
"""

    response = model.generate_content(prompt)

    answer = response.text.strip()

    answer = answer.replace("```json", "").replace("```", "").strip()

    return json.loads(answer)
