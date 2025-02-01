#!/usr/bin/python3
# https://github.com/openai/openai-python

import openai
from openai import OpenAI

import os

# Set your OpenAI API key
# export OPENAI_API_KEY="your_api_key"


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    #organization="org-Z...w",
    #project='proj_j...S',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini",
)


