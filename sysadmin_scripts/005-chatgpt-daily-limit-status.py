#!/usr/bin/python3
# https://github.com/openai/openai-python

import openai
import os

# Set your OpenAI API key
# export OPENAI_API_KEY="your_api_key"


openai.api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted

def get_usage():
    try:
        # Get the usage details
        usage = openai.api_request("usage")
        print("Usage details:")
        print(usage)
    except Exception as e:
        print(f"An error occurred: {e}")

get_usage()

