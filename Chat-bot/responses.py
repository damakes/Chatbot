# response.py
import random


# Responses
R_BEGIN = "Hello!"
R_END = "See you!"
R_EXPRESSION = "You're welcome!"
R_ELEVATOR = "I'm doing fine, and you?"
R_EATING = "I don't like anything because I'm a bot obviously!"
R_ADVICE = "Go to the internet and type exactly what you wrote there!"

# List of trigger words for single response
R_BEGIN_LIST = ['hello', 'hi', 'hey', 'sup', 'heyo']
R_END_LIST = ['bye', 'goodbye']
R_EXPRESSION_LIST = ['thank', 'thanks']
R_ELEVATOR_LIST = ['how', 'are', 'you', 'doing']
R_EATING_LIST = ['what', 'you', 'eat']
R_ADVICE_LIST = ['give', 'advice']

# Required words for response
R_ELEVATOR_REQUIRED_WORDS = ['how']
R_EATING_REQUIRED_WORDS = ['you', 'eat']
R_ADVICE_REQUIRED_WORDS = ['advice']

# Randomized response function, triggerd by required words
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


    