import json
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


class MemoryManager:

    def __init__(self, memory):

        self.memory = memory

    def process(self, user_text):

        prompt = f"""
You are a memory extraction AI.

Extract important long-term memories from the user's message.

Return ONLY valid JSON.

Format:

{{
    "save": true,
    "category": "",
    "key": "",
    "value": "",
    "importance": 8
}}

If nothing important:

{{
    "save": false
}}

User:

{user_text}
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )

            data = json.loads(
                response.choices[0].message.content
            )

            if data.get("save"):

                self.memory.save_memory(
                    category=data.get("category", "general"),
                    key=data.get("key"),
                    value=data.get("value"),
                    importance=data.get("importance", 5)
                )

        except Exception as e:
            print("Memory Error:", e)
                # ---------------- Memory Questions ---------------- #

    def get_answer(self, user_text):

        memories = self.memory.get_all_memories()

        if not memories:
            return None

        memory_text = ""

        for category, key, value, importance in memories:
            memory_text += f"{key}: {value}\n"

        prompt = f"""
You are Neo AI.

Answer ONLY using the user's saved memories.

If the answer is not available, return exactly:

NONE

Saved Memories:

{memory_text}

Question:

{user_text}
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )

            answer = response.choices[0].message.content.strip()

            if answer.upper() == "NONE":
                return None

            return answer

        except Exception as e:
            print("Memory Search Error:", e)
            return None

    # ---------------- Memory Context ---------------- #

    def get_context(self):

        memories = self.memory.get_all_memories()

        if not memories:
            return ""

        context = "User Memories:\n\n"

        for category, key, value, importance in memories:

            context += (
                f"- [{category}] "
                f"{key}: {value}\n"
            )

        return context