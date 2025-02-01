#!/usr/bin/python3
# https://github.com/openai/openai-python

import os

# Set your OpenAI API key
# export OPENAI_API_KEY="your_api_key"
from openai import OpenAI

my_api_key = os.getenv("OPENAI_API_KEY")

if my_api_key:
  client = OpenAI(
    api_key = my_api_key
  )
else:
    print("OPENAI_API_KEY is not set")
    exit()

def chat_with_gpt(prompt, model="gpt-4o-mini"):
    try:
        # Make the API call
        completion = client.chat.completions.create(
                store = True, #enable the storage of chat completion outputs for future reference
                model = model,
                messages = [
                  {"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}
                ],
                temperature = 0.7,    # Adjust creativity level (0-1)
                max_tokens = 100     # Adjust token limit
        )
        # Extract and return the response
        return completion.choices[0].message.content 
    except Exception as e:
        return f"An error occured {e}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    reply = chat_with_gpt(prompt)
    print(f"ChatGTP:\n{reply}\n")

