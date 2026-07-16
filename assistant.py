from memory import Memory
from memory_manager import MemoryManager

from speech import SpeechEngine
from chat_handler import ChatHandler
from command_handler import CommandHandler


class AIAssistant:

    def __init__(self):

        self.speech = SpeechEngine()

        self.memory = Memory()
        self.memory_manager = MemoryManager(self.memory)

        self.chat_handler = ChatHandler()
        self.command_handler = CommandHandler()

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

If the user speaks English,
reply in English.
"""

        self.conversation_history = self.memory.load_chat(30)

        print("✅ Neo AI Ready")

    # ---------------- Voice ---------------- #

    def speak(self, text):

        self.speech.set_voice(self.voice_enabled)
        self.speech.speak(text)

    # ---------------- Main ---------------- #

    def get_response(self, user_input):

        if not user_input.strip():
            return ""

        # Save User Message
        self.memory.save_chat("user", user_input)

        # Process Memory
        self.memory_manager.process(user_input)

        # Memory Questions
        memory_answer = self.memory_manager.get_answer(user_input)

        if memory_answer:

            self.memory.save_chat("assistant", memory_answer)

            self.speak(memory_answer)

            return memory_answer

        # Refresh Conversation
        self.conversation_history = self.memory.load_chat(30)

        memory_context = self.memory_manager.get_context()

        system_message = {
            "role": "system",
            "content": self.system_prompt + "\n\n" + memory_context
        }

        # -------- Commands -------- #

        tool_response = self.command_handler.handle(user_input)

        if tool_response:

            self.memory.save_chat("assistant", tool_response)

            self.speak(tool_response)

            return tool_response

        # -------- AI -------- #

        try:

            ai_reply = self.chat_handler.chat(
                system_message,
                self.conversation_history,
                user_input
            )

        except Exception as e:

            print("Groq Error:", e)

            ai_reply = "Sorry, I couldn't generate a response."

        self.memory.save_chat("assistant", ai_reply)

        self.speak(ai_reply)

        return ai_reply