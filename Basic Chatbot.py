#Import required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot, my chatbot name is 'Rush'
bot = ChatBot(
    'Rush',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few response 
trainer.train(
    [
         ' Hi ',
         ' Hello ',
         ' How are you ',
         " I'm Good ",
         ' Is anyone there? ',
         ' Hi there, how can I help? ',
         ' What is your name? ',
         " I'm Rush, Rushi's bot ",
         ' Who are you? ',
         ' My name is Rush ',
         ' Are you a robot? ',
         " Yes I am a robot, but I'm a good one. ",
         ' Who made you? ',
         ' Rushi made me ',
         ' What is the purpose of creating you?',
         ' Rushi had the job of building a chatbot and he created me.I thank Rushi. ',
         ' What programming language was used to create you? ',
         ' Rushi created me using Python ',
         ' I want to learn how to create chatbots ',
         ' Great, this should help get you started : https://chatterbot.readthedocs.io/en/stable/ ',
         ' Thanks ',
         ' Happy to help! ',
         ' Thank you ',
         ' Any time! ',
         " That's helpful ",
         ' My pleasure ',
         ' Bye ',
         ' See you later, thanks for visiting ',
         ' See you later ',
         ' Have a nice day ',
         ' Goodbye ',
         ' Bye! Come back again soon. '
    ]
)

# Get a response for some unexpected input
while True:
    req = input('You :')
    response = bot.get_response(req)
    print('Bot :',response)

