import google.generativeai as palm
import configparser

def genAI(inputInfo):

    palm.configure(api_key='AIzaSyD0ZfvZkFFCbFwwSH29rslG0JkmTgn7SVU')
    model = palm.GenerativeModel()
    response = str(model.generate_content(inputInfo + "Give A Summary & Give Recommendations to resolve."))

    return response