import google.generativeai as palm
import configparser

def create_chatbot(input_prompt):
  # Read the API key from the config.ini file
  config = configparser.ConfigParser()
  config.read('config.ini')
  api_key = config.get('API', 'gemini_api_key')

  # Set up the PaLM API key
  palm.configure(api_key=api_key)

  model = palm.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(input_prompt)

  return response.text
