import nltk 
from nltk.chat.util import Chat, reflections 
import tkinter as tk 
from tkinter import scrolledtext 
# Define chatbot responses using pairs 
pairs = [ [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]], 
            [r"how are you?", ["I'm just a bot, but I'm doing fine! How about you?", "I'm a chatbot, so I'm always good! How are you?"]], 
            [r"(.*) your name?", ["I'm a chatbot, here to assist you."]], 
            [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]], 
            [r"(.*)", ["I'm not sure how to respond to that. Could you rephrase?"]] 
        ] 
# Create chatbot 
chatbot = Chat(pairs, reflections) 
# Function to handle user input and display response 
def send_message(): 
    user_input = user_entry.get() 
    chat_history.insert(tk.END, f"You: {user_input}\n") 
    response = chatbot.respond(user_input) 
    chat_history.insert(tk.END, f"Bot: {response}\n\n") 
    user_entry.delete(0, tk.END)
    
# GUI setup 
root = tk.Tk() 
root.title("Simple Chatbot") 
# Scrolled text widget for chat history 
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15) 
chat_history.pack(padx=10, pady=10) 
# Entry widget for user input 
user_entry = tk.Entry(root, width=40) 
user_entry.pack(padx=10, pady=5) 
# Button to send the message 
send_button = tk.Button(root, text="Send", command=send_message) 
send_button.pack(pady=5) 
# Start the GUI main loop 
root.mainloop()