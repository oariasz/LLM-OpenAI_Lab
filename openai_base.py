from time import sleep
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_    = load_dotenv(find_dotenv())    # read local .env file


'''
EXAMPLE OF RESPONSE STRUCTURE 
{
    {
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-3.5-turbo-1106",
    "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "total_tokens": 20
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "\n\nThis is a test!"
            },
            "logprobs": null,
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
'''


# Set the API KEY
# OPENAI_API_KEY = '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'
OPENAI_API_KEY = os.getenv("API_KEY")



def get_completion(prompt, client, model='gpt-3.5-turbo-1106', temp=0):  #  model='gpt-3.5-turbo' has been DEPRECATED
    # Build the message prompt
    messages = [{'role': 'assistant', 'content': prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temp,      # this is the degreee of randomness    
    )
    # print ('sleeping...')
    sleep(1)
  
    return response.choices[0].message.content

def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == 'posix':  # Linux and MacOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')


####### MAIN #######
client = OpenAI(api_key=OPENAI_API_KEY)

# Building the prompt
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""

prompt = 'What is the tallest waterfall on Earth?'
response = get_completion(prompt, client) # call your function



clear_screen()
print ('--- AriHer Chat GPT ---\n\n')

print('Prompt:', prompt)
print ('Ansuer:', response)

