import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GENERATIVE_AI_API_KEY"])


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Give me a list of super annuation funds that invest in Eduaction")
print(response.text)