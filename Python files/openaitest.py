import os
import openai
openai.api_key = "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"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)