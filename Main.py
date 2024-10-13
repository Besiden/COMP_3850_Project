## How to use
## run this command in terminal on your PC and replace the "YOUR_API_KEY" with the api key
## Alex has sent you 


## Windows powershell : $env:GENERATIVE_AI_API_KEY = "YOUR_API_KEY"
## Linux/mac : export GENERATIVE_AI_API_KEY="YOUR_API_KEY"

## The prompt will be printed in the terminal

## requires python to be installed on your machine 


import google.generativeai as genai
import os
import glob

genai.configure(api_key=os.environ["GENERATIVE_AI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

import json
from http.server import BaseHTTPRequestHandler, HTTPServer



class RequestHandler(BaseHTTPRequestHandler):

   
    def do_OPTIONS(self):
        # Handle CORS preflight request
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/process':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # Parse the received data
            data = json.loads(post_data)
            super_selected = data.get('superSelected')
            esg_selected = data.get('esgSelected', [])

            # Get the processed message based on selection
            response_message = self.process_selection(super_selected, esg_selected)
            
            # Send the response to the client
            self.send_response_message(response_message)

    def process_selection(self, super_selected, esg_selected):
        """
        This function processes the Super or ESG selection
        and returns the corresponding message.
        """
        # Initialize the message
        response_message = 'no valid combination selected' 
        # Should be re-written to null check(None Selected) and then pass input through to Generate AI function
        
        if len(esg_selected) > 0:
            print(esg_selected)
            response = model.generate_content("Output a list of Superfunds that invest in the following Environtmental Social and Governance themes: ".join(str(esg_selected)))
            return response.text

        if super_selected:
            # Upload all files in the directory
            directory = f"Documents/{super_selected}/"
            files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            uploaded_files = []  # Initialize an empty list to store uploaded file references

            for file in files:
                uploaded_file = genai.upload_file(file)  # Upload each file individually
                uploaded_files.append(uploaded_file)  # Add the uploaded file reference to the list

            # Generate a prompt using all uploaded files
            # prompt = ["Give me a basic summary of how " + str(super_selected) + " makes ESG conscious investments. The response should be less than 150 words and based on the content provided.", *uploaded_files]

            # Generate the response
            response = model.generate_content(["Give me a basic summary of how " + str(super_selected) + " makes ESG conscious investments. The response should be less than 500 words and use quotes from the files provided.", *uploaded_files])
            print(response.text)
            super_selected = False  # Reset the variable
            response_message = response.text

        return response_message    
        

    def send_response_message(self, message):
        """
        This function sends the response message to the client.
        """
        # Create response with the message
        response = {'value': message}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)  # Serve on localhost:8000
    httpd = server_class(server_address, handler_class)
    print('Starting server on http://localhost:8000')
    httpd.serve_forever()


if __name__ == '__main__':
    run()