#!/usr/bin/env python3

import argparse
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
def get_gemini_response(query):
    url = os.getenv('GEMINI_API_URL')
    api_key = os.getenv('GEMINI_API_KEY')

    with open('prompt.txt', 'r') as file:
        prompt_template = file.read()
    
    prompt = prompt_template.format(query=query)
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(f"{url}?key={api_key}", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json().get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No text found')
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    parser = argparse.ArgumentParser(description="Ask Jarvis anything!")
    parser.add_argument('query', type=str, nargs='+', help="The question for Jarvis")

    args = parser.parse_args()
    query = ' '.join(args.query)

    response = get_gemini_response(query)
    print(response)

if __name__ == "__main__":
    main()
