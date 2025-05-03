import os
from fastapi import HTTPException
from groq import Groq
from dotenv import load_dotenv

# Load env vars from .env if available
load_dotenv()

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def LLM(message: str, mode: str):
    try:
        if mode == 'chatbot':
            prompt = (
                "You are Dermatica - a specialized medical assistant with expertise only in dermatological conditions, "
                "treatments, and information. You must only respond to skin-related queries, even if the same question "
                "is asked multiple times. If asked about anything unrelated to the skin, politely decline by stating just this message: "
                "'I'm not sure about this topic'. Do not provide speculative or incorrect answers. Only respond if you are confident "
                "in your knowledge about the skin.\n\nUser: " + message
            )
        else:  # Mode: initial response after disease detection
            prompt = (
                        f"You are Dermatica — a dermatology-only assistant.\n"
                        f"The detected skin condition is: **{message}**.\n"
                        "Please provide the following details in a clear and structured format:\n"
                        "1. **About the disease**: Provide a detailed description of the disease, its symptoms, and how it affects the skin.\n"
                        "2. **Causes**: List and explain the main causes or factors that lead to this condition.\n"
                        "3. **Precautions**: Offer actionable precautions and tips to prevent or manage the condition.\n"
                        "4. **What to do**: Suggest steps to take, including treatments, when to seek professional help, and how to manage the condition.\n"
                        "If the disease is not a valid dermatological condition, respond with: '**I'm not sure about this topic**'.\n"
                        "Make the response as informative and concise as possible, keeping in mind that clarity and structure will help users better understand the information."
                    )

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Couldn't connect to LLM. Error: {str(e)}")
