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
# response = model.generate_content("Say Hello")
# print(response.text)



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

        # Check for specific ESG combinations
        if len(esg_selected) == 3:
            response_message = 'all ESG options selected'
        elif 'ESG Option 1' in esg_selected and 'ESG Option 2' in esg_selected:
            response_message = 'hello'  # If ESG 1 and ESG 2 are selected
        elif 'ESG Option 1' in esg_selected and 'ESG Option 3' in esg_selected:
            response_message = 'outcome for 1 and 3'
        elif 'ESG Option 2' in esg_selected and 'ESG Option 3' in esg_selected:
            response_message = 'outcome for 2 and 3'
        elif 'ESG Option 1' in esg_selected:
            response_message = 'only ESG Option 1 selected'
        elif 'ESG Option 2' in esg_selected:
            response_message = 'only ESG Option 2 selected'
        elif 'ESG Option 3' in esg_selected:
            response_message = 'only ESG Option 3 selected'

        # Handle Super options
        if super_selected:
            if super_selected == 'Super Option 1':
                AusSuperPDF = genai.upload_file("AusSuperESG.pdf")
                response = model.generate_content(["Give me a basic outline of the ESG Policy of Australian Super based on the provided PDF , in less than 100 words", AusSuperPDF])
                print(response.text)
                response_message = response.text


            elif super_selected == 'Super Option 2':
                response_message = 'cat'
            elif super_selected == 'Super Option 3':
                response_message = 'Super3'

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
    

