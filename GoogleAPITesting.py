## How to use
## run this command in terminal on your PC and replace the "YOUR_API_KEY" with the api key
## Alex has sent you 


## Windows powershell : $env:GENERATIVE_AI_API_KEY = "YOUR_API_KEY"
## Linux/mac : export GENERATIVE_AI_API_KEY="YOUR_API_KEY"

## Modify Line 21 To the desired prompt
## The prompt will be printed in the terminal

## requires python to be installed on your machine 


import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GENERATIVE_AI_API_KEY"])


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Give me a list of super annuation funds that invest in Eduaction")
print(response.text)