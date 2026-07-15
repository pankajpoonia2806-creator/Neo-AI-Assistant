import os
import threading
from gtts import gTTS
import playsound


class SpeechEngine:

    def __init__(self):
        self.voice_enabled = True

    def set_voice(self, enabled: bool):
        self.voice_enabled = enabled

    def speak(self, text):

        print("Neo:", text)

        if not self.voice_enabled:
            return

        def speak_thread():

            try:

                filename = "neo_response.mp3"

                tts = gTTS(
                    text=text,
                    lang="hi",
                    slow=False
                )

                tts.save(filename)

                playsound.playsound(filename)

                if os.path.exists(filename):
                    os.remove(filename)

            except Exception as e:
                print(e)

        threading.Thread(
            target=speak_thread,
            daemon=True
        ).start()