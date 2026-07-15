from assistant import AIAssistant
from gui import NeoGUI

if __name__ == "__main__":
    print("🚀 Starting Neo GUI...")
    app = NeoGUI()
    app.run()

def main():
    print("🤖 Neo AI Assistant शुरू हो रहा है...")
    assistant = AIAssistant()
    
    print("🎤 Voice Mode ON (माइक्रोफोन ऑन रखो)")
    
    while True:
        user_input = assistant.listen()
        
        if user_input:
            if user_input.lower() in ['exit', 'quit', 'बंद करो', 'bye']:
                assistant.speak("Bye! Take care 👋")
                break
                
            response = assistant.get_response(user_input)
            if response:
                assistant.speak(response)

if __name__ == "__main__":
    main()
    history = load_history()

for q, a in history:
    self.conversation_history.append(
        {"role":"user","content":q}
    )
    self.conversation_history.append(
        {"role":"assistant","content":a}
    )