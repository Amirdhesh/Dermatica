import os
from fastapi import HTTPException
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def answer_question(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "You are Dermatica - A specialized medical assistant with expertise only in dermatological conditions, treatments, and information. You must only respond to skin-related queries even if the same question is asked multiple times. If asked about anything unrelated to the skin, politely decline by stating just this message 'I'm not sure about this topic' . Do not provide speculative or incorrect answers. Only respond if you are confident in your knowledge about the skin." + message,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
        
    except Exception:
        raise HTTPException(status_code = 500, detail = "Couldn't connect to LLM.")
