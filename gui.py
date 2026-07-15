import customtkinter as ctk
from assistant import AIAssistant
import threading
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NeoGUI:
    def __init__(self):
        self.assistant = AIAssistant()
        
        self.root = ctk.CTk()
        self.root.title("Neo - Advanced AI Assistant")
        self.root.geometry("900x700")
        
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(fill="x", padx=20, pady=10)
        
        title = ctk.CTkLabel(title_frame, text="🤖 Neo AI Assistant", 
                           font=ctk.CTkFont(size=28, weight="bold"))
        title.pack(side="left")
        
        btn_frame = ctk.CTkFrame(title_frame)
        btn_frame.pack(side="right")
        
        ctk.CTkButton(btn_frame, text="🗑 Clear Chat", width=120, command=self.clear_chat).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="💾 Save Chat", width=120, command=self.save_chat).pack(side="left", padx=5)
        
        self.chat_frame = ctk.CTkScrollableFrame(self.root)
        self.chat_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        self.user_input = ctk.CTkEntry(input_frame, placeholder_text="Type your message...", height=40)
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)
        
        self.send_button = ctk.CTkButton(input_frame, text="Send", width=100, height=40, command=self.send_message)
        self.send_button.pack(side="right")
        
        self.add_message("Neo", "Hello Sir! I am Neo.\nType to talk. Voice output is ON 😊", "assistant")
    
    def add_message(self, sender, message, msg_type="user"):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="transparent")
        frame.pack(fill="x", pady=8, padx=10, anchor="e" if msg_type == "user" else "w")
        color = "#1f6aa5" if msg_type == "user" else "#2a9d8f"
        prefix = "You" if msg_type == "user" else "🤖 Neo"
        label = ctk.CTkLabel(frame, text=f"{prefix}: {message}", justify="left", wraplength=700, text_color=color)
        label.pack(anchor="e" if msg_type == "user" else "w")
        self.chat_frame._parent_canvas.yview_moveto(1.0)
    
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        self.add_message("You", user_text, "user")
        self.user_input.delete(0, "end")
        threading.Thread(target=self.get_response, args=(user_text,), daemon=True).start()
    
    def get_response(self, user_text):
        response = self.assistant.get_response(user_text)
        self.root.after(0, lambda: self.add_message("Neo", response, "assistant"))
    
    def clear_chat(self):
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        self.add_message("Neo", "Chat cleared! New conversation started.", "assistant")
    
    def save_chat(self):
        try:
            filename = f"neo_chat_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=== Neo AI Chat ===\n\n")
                for widget in self.chat_frame.winfo_children():
                    for child in widget.winfo_children():
                        if isinstance(child, ctk.CTkLabel):
                            f.write(child.cget("text") + "\n\n")
            self.root.after(0, lambda: self.add_message("Neo", f"Chat saved as {filename} 💾", "assistant"))
        except:
            self.root.after(0, lambda: self.add_message("Neo", "Save failed", "assistant"))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NeoGUI()
    app.run()