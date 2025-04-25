import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create the chatbot
chatbot = ChatBot('SupportBot')

# Train with ChatterBot corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.english.greetings',
    'chatterbot.corpus.english.conversations'
)

# Custom Q&A for technical and academic help
custom_data = [
    "How do I reset my password?",
    "Go to settings and click 'Reset Password'.",
    
    "What is Python?",
    "Python is a popular programming language known for its simplicity.",

    "How can I install Python?",
    "You can install Python from python.org by downloading the latest version.",

    "What is a function in programming?",
    "A function is a block of code that only runs when it is called.",

    "How do I check my exam results?",
    "Log into the academic portal and click on 'Results'."
]

# Train with custom data
custom_trainer = ListTrainer(chatbot)
custom_trainer.train(custom_data)

# Function to get response from chatbot
def get_response():
    query = user_input.get()
    response = chatbot.get_response(query)
    chat_window.insert(tk.END, "You: " + query + '\n')
    chat_window.insert(tk.END, "Bot: " + str(response) + '\n')
    user_input.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("SupportBot")

# Create chat window (Text widget)
chat_window = tk.Text(root, height=15, width=50)
chat_window.pack(pady=10)

# Create user input field (Entry widget)
user_input = tk.Entry(root, width=40)
user_input.pack(pady=10)

# Create a button to send message
send_button = tk.Button(root, text="Send", width=20, command=get_response)
send_button.pack(pady=5)

# Run the GUI application
root.mainloop()
