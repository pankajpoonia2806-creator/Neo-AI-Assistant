from groq import Groq
from config import GROQ_API_KEY


class ChatHandler:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def chat(self, system_message, conversation_history, user_input):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                system_message,
                *conversation_history,
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return response.choices[0].message.content.strip()