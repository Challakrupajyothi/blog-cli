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

# Simple interaction loop
print("Hello! I'm SupportBot. Ask me anything (type 'exit' to quit):")
while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    response = chatbot.get_response(query)
    print("Bot:", response)
