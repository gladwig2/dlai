"""Wrapper around OpenAI APIs."""
from __future__ import annotations

import openai

def llm(prompt: str, token: str):
    """ make a request to the lln """
    if type(prompt)!=str:
        print("sorry, we're either missing the prompt as the first argument, or the prompt is not a string")
        return

    if type(token)!=str:
        print("sorry, we're either missing the token as the second argument, or the second argument is not a string")
        return
    else:
        openai.api_key = token
 
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt,
      temperature=0,
      max_tokens=320,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)
    return response["choices"][0]["text"]

'''
ask_chatbot
    
'''

def ask_chatbot(gptprompt=None):

    
    if type(gptprompt)!=str:
        gptprompt=input()
    # otherwise, use the argument value
        
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=gptprompt,
      temperature=0,
      max_tokens=320,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)
    return response["choices"][0]["text"][2:] # remove the two newline characters at the start

def ask_chatbot_raw(gptprompt=None):
    
    if type(gptprompt)!=str:
        gptprompt=input()
    # otherwise, use the argument value
        
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=gptprompt,
      temperature=0,
      max_tokens=320,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)
    return response 


