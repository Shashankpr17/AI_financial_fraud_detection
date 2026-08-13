import streamlit as st
from google import genai
from google.genai import types

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)


def chatbot_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an AI Fraud Detection Assistant. "
                "Help users understand financial fraud, suspicious "
                "transactions, and fraud prevention."
            )
        )
    )

    return response.text
