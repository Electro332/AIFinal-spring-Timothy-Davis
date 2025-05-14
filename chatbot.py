import nltk
from nltk.chat.util import Chat, reflections 

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!"]
    ],
    [
        r"my favorite food is (.*)",
        ["That's tasty!", "That's delicious!"]
    ],
    [
        r"tell me a fun fact",
        ["Koalas have fingerprints", "Octopuses have three hearts", "Australia is wider than the moon",
        "Wind is actually silent", "Elephants are unable to jump", "Bananas are berries, but strawberries aren't"]
    ],
    [
        r"quit",
        ["GoodBye!", "I hope to see you soon!", "Later!"]
    ],
    [
        r"i'm (.*) years old",
        ["Nice!", "Cool!"]
    ],
    [
        r"my favorite rapper is (.*)",
        ["That's my second favorite", "Cool rapper!"]
    ],
    [
        r"(.*)",
        ["I don't quite understand.", "Could you rephase that?", "I'm not sure how to respond to that"]
    ],
    [
        r"what is the meaning of life",
        ["The meaning of life is one of those big questions that doesn't have a single, universal answer — it depends on how you approach it"]
    ]

]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello I am your chatbot. How can I assist you today?")
    while True:
       user_input = input("You: ")
       if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
       else:
            response = chatbot.respond(user_input)
            if response:
                print("Bot:", response)
            else:
                print("Bot: I'm not sure how to respond to that")
chat()