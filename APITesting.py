# Testing Stuff

import requests

def query_gemini_ai(api_key, prompt):
    url = "https://gemini.googleapis.com/v1/models/gemini-<626565544050>:predict"  # Replace <model_id> with the actual model ID

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "instances": [{"input": prompt}],  # Replace 'input' with the appropriate field as required by the API
        "parameters": {
            "temperature": 0.5,  # Adjust as needed
            "max_tokens": 150  # Adjust as needed
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    

query_gemini_ai('AIzaSyBtgibAIPmioz7yUprwygtbTYWacwsDE04', "What is 1 + 1")