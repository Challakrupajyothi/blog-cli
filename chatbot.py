from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the chatbot
chatbot = ChatBot('SupportBot')

# Train with ChatterBot corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.english.greetings',
    'chatterbot.corpus.english.conversations'
)

# Set up the GUI
def get_response():
    user_input = user_input_field.get()
    bot_response = chatbot.get_response(user_input)
    chat_history.config(state=NORMAL)
    chat_history.insert(END, "You: " + user_input + '\n')
    chat_history.insert(END, "Bot: " + str(bot_response) + '\n')
    chat_history.config(state=DISABLED)
    user_input_field.delete(0, END)

# Create main window
root = Tk()
root.title("SupportBot Chat")
root.geometry("400x500")

# Create the chat history box
chat_history = Text(root, bd=1, bg="light gray", width=50, height=20, wrap=WORD)
chat_history.config(state=DISABLED)
chat_history.pack(pady=20)

# Create the user input field
user_input_field = Entry(root, bd=1, bg="white", width=40)
user_input_field.pack(pady=10)

# Create the send button
send_button = Button(root, text="Send", width=10, height=2, command=get_response)
send_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
