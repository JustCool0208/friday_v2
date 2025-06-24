import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
# for m in genai.list_models():
#     print(m.name)


def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
