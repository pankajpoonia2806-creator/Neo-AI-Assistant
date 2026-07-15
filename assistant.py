from groq import Groq
from config import GROQ_API_KEY

from memory import Memory
from memory_manager import MemoryManager
from tools import Tools
from pc_control import PCControl
from internet import Internet
from speech import SpeechEngine


client = Groq(api_key=GROQ_API_KEY)


class AIAssistant:

    def __init__(self):
        self.speech = SpeechEngine()

        self.memory = Memory()

        self.memory_manager = MemoryManager(
            self.memory
        )

        self.voice_enabled = True

        self.system_prompt = """
You are Neo AI.

You are an advanced personal AI assistant.

Always remember previous conversations.

Use saved memories naturally.

Be friendly.

Never ignore memory.

Answer in the user's language.

If the user speaks Hindi,
reply in Hindi.

If English,
reply in English.
"""

        self.conversation_history = (
            self.memory.load_chat(30)
        )

        print("✅ Neo AI Ready")

    # ---------------- Voice ---------------- #

    def speak(self, text):
     self.speech.set_voice(self.voice_enabled)
     self.speech.speak(text)
            # ---------------- Main ---------------- #

    def get_response(self, user_input):

        if not user_input:
            return ""

        # Save user message
        self.memory.save_chat("user", user_input)

        # Auto memory extraction
        self.memory_manager.process(user_input)

        # Direct memory questions
        memory_answer = self.memory_manager.get_answer(user_input)

        if memory_answer:
            self.memory.save_chat("assistant", memory_answer)
            self.speak(memory_answer)
            return memory_answer

        # Conversation history
        self.conversation_history = self.memory.load_chat(30)

        # Memory context
        memory_context = self.memory_manager.get_context()

        system_message = {
            "role": "system",
            "content": (
                self.system_prompt
                + "\n\n"
                + memory_context
            )
        }

        # -------- Try Tools -------- #

        tool_response = self._try_tool(user_input)

        if tool_response:

            self.memory.save_chat(
                "assistant",
                tool_response
            )

            self.speak(tool_response)

            return tool_response
                # ---------------- AI ---------------- #

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    system_message,
                    *self.conversation_history,
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                temperature=0.7,
                max_tokens=1024
            )

            ai_reply = response.choices[0].message.content.strip()

        except Exception as e:

            print("Groq Error:", e)

            ai_reply = (
                "Sorry, I couldn't generate a response."
            )

        # Save Assistant Reply

        self.memory.save_chat(
            "assistant",
            ai_reply
        )

        self.speak(ai_reply)

        return ai_reply
        # ---------------- Tools ---------------- #

    def _try_tool(self, user_input):

        lower = user_input.lower()

        # -------- Chrome -------- #

        if "open chrome" in lower:
            return PCControl.open_chrome()

        # -------- Notepad -------- #

        if "open notepad" in lower:
            return PCControl.open_notepad()

        # -------- Calculator -------- #

        if "open calculator" in lower:
            return PCControl.open_calculator()

        # -------- Explorer -------- #

        if "open explorer" in lower:
            return PCControl.open_explorer()

        # -------- VS Code -------- #

        if "open vscode" in lower or "open vs code" in lower:
            return PCControl.open_vscode()

        # -------- Weather -------- #

        if any(word in lower for word in [
            "weather",
            "temperature",
            "temp",
            "मौसम"
        ]):

            city = "Delhi"

            words = user_input.split()

            for i, word in enumerate(words):

                if word.lower() in [
                    "in",
                    "of",
                    "ka",
                    "mein",
                    "में"
                ] and i + 1 < len(words):

                    city = words[i + 1].capitalize()
                    break

            return Tools.get_weather(city)

        # -------- Time -------- #

        if any(word in lower for word in [
            "time",
            "clock",
            "samay",
            "baje",
            "समय",
            "घड़ी"
        ]):

            return Tools.get_time()

        # -------- Wikipedia -------- #

        if any(word in lower for word in [
            "wiki",
            "wikipedia",
            "what is",
            "क्या है"
        ]):

            query = (
                user_input
                .replace("wiki", "")
                .replace("wikipedia", "")
                .replace("what is", "")
                .replace("क्या है", "")
                .strip()
            )

            if not query:
                query = "India"

            return Tools.wikipedia_search(query)
              # -------- Internet Search -------- #

        internet_keywords = [
            "who is",
            "what is",
            "search",
            "google",
            "latest",
            "today",
            "news",
            "price",
            "information",
            "tell me about"
        ]

        if any(word in lower for word in internet_keywords):

            result = Internet.search(user_input)

            if result:

                prompt = f"""
Use the following internet search results to answer the user.

Search Results:

{result}

User Question:

{user_input}

Give a clear, short and accurate answer.
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
                        temperature=0.3,
                        max_tokens=500
                    )

                    return response.choices[0].message.content

                except Exception:
                    return result

            return "Sorry, I couldn't find anything on the internet."

        return None