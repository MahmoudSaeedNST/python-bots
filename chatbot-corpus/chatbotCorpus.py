from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

chatbot = ChatBot('Mahmoud',
                  logic_adapters=[
                      'chatterbot.logic.BestMatch',
                      'chatterbot.logic.MathematicalEvaluation'
                  ],
                  database_uri='sqlite:///database.sqlite3')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.english'
)

# Now let's get a response to a greeting
while True:
    humen = input("You: ")
    response = chatbot.get_response(humen)
    print("Bot: ", response)