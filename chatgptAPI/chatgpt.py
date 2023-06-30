from flask import Flask, request
import openai

openai.api_key = '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'

def talk_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    chat_reply = response.choices[0].text.strip()
    return chat_reply