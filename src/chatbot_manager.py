import google.generativeai as palm
import configparser

def create_chatbot(input_prompt, api_key):
  # Set up the PaLM API key
  palm.configure(api_key=api_key)

  model = palm.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(input_prompt)

  return response.text
