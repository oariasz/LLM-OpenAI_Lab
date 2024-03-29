from time import sleep
from openai import OpenAI
import os
from IPython.display import display, HTML
from dotenv import load_dotenv, find_dotenv
_    = load_dotenv(find_dotenv())    # read local .env file

# PRINCIPLES WORKING WITH CHAT COMPLETION
# 1. Clear and especific instructions
# 2. Give the model time to think


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
# OPENAI_API_KEY = *** NEVER DISCLOSE THE API KEY HERE, GETTING IT FROM ENV ***
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

def get_example_prompt(id):
    prompt = []
    
    # ID = 0     // Initial example
    prompt.append('What is the tallest waterfall on Earth?')
    
    # ID = 1    // Tactic 1: Use delimiters to clearly indicate distinct parts of the input
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
    p = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence.
    ```{text}```
    """
    prompt.append(p)
    
    # ID = 2    // Tactic 2: Ask for a structured output
    p = f"""
    Generate a list of the three most life-changing book titles you night see on the internet along \ 
    with their authors, genres and year of publication. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre, year.
    """
    prompt.append(p)

    # ID = 3    // Ask the model to check whether conditions are satisfied
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some \ 
    water boiling. While that's happening, \ 
    grab a cup and put a tea bag in it. Once the water is \ 
    hot enough, just pour it over the tea bag. \ 
    Let it sit for a bit so the tea can steep. After a \ 
    few minutes, take out the tea bag. If you \ 
    like, you can add some sugar or milk to taste. \ 
    And that's it! You've got yourself a delicious \ 
    cup of tea to enjoy.
    """
    p = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, \ 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \ 
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """
    prompt.append(p)
    
   
    # ID = 4    //  Tactic 4: "Few-shot" prompting
    p = f"""
    Your task is to answer in a consistent style.

    <child>: Teach me about patience.

    <grandparent>: The river that carves the deepest \ 
    valley flows from a modest spring; the \ 
    grandest symphony originates from a single note; \ 
    the most intricate tapestry begins with a solitary thread.

    <child>: Teach me about resilience.
    """
    prompt.append(p)
    
    # ID = 5    //  Tactic 4: Iterative improving of the prompts
    
    fact_sheet_chair = """
        OVERVIEW
        - Part of a beautiful family of mid-century inspired office furniture, 
        including filing cabinets, desks, bookcases, meeting tables, and more.
        - Several options of shell color and base finishes.
        - Available with plastic back and front upholstery (SWC-100) 
        or full upholstery (SWC-110) in 10 fabric and 6 leather options.
        - Base finish options are: stainless steel, matte black, 
        gloss white, or chrome.
        - Chair is available with or without armrests.
        - Suitable for home or business settings.
        - Qualified for contract use.

        CONSTRUCTION
        - 5-wheel plastic coated aluminum base.
        - Pneumatic chair adjust for easy raise/lower action.

        DIMENSIONS
        - WIDTH 53 CM | 20.87”
        - DEPTH 51 CM | 20.08”
        - HEIGHT 80 CM | 31.50”
        - SEAT HEIGHT 44 CM | 17.32”
        - SEAT DEPTH 41 CM | 16.14”

        OPTIONS
        - Soft or hard-floor caster options.
        - Two choices of seat foam densities: 
        medium (1.8 lb/ft3) or high (2.8 lb/ft3)
        - Armless or 8 position PU armrests 

        MATERIALS
        SHELL BASE GLIDER
        - Cast Aluminum with modified nylon PA6/PA66 coating.
        - Shell thickness: 10 mm.
        SEAT
        - HD36 foam

        COUNTRY OF ORIGIN
        - Italy
    """
    p = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Technical specifications: ```{fact_sheet_chair}```
    """
    prompt.append(p)
    
    
    
    return prompt[id]
    

####### MAIN #######

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT_NUMBER = 3

prompt = get_example_prompt(PROMPT_NUMBER)
response = get_completion(prompt, client) # call your function



clear_screen()
print ('--- AriHer Chat GPT ---\n\n')

print('Prompt:', prompt)
print ('Ansuer:', response)

# Despliega la respuesta en HTML
if PROMPT_NUMBER==5: 
    display(HTML(response))