# main.py
import re
import responses as res
import polarity as polarity

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response(res.R_BEGIN, res.R_BEGIN_LIST , single_response=True)
    response(res.R_END, res.R_END_LIST, single_response=True)
    response(res.R_EXPRESSION , res.R_EXPRESSION_LIST, single_response=True)

    # Responses RQ + def unk()
    response(res.R_ELEVATOR, res.R_ELEVATOR_LIST, res.R_ELEVATOR_REQUIRED_WORDS)
    response(res.R_ADVICE, res.R_ADVICE_LIST, res.R_ADVICE_REQUIRED_WORDS)
    response(res.R_EATING, res.R_EATING_LIST, res.R_EATING_REQUIRED_WORDS)

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # Print each key-value pair on a new line
    for key, value in highest_prob_list.items():
        print(f"{('-_')*50}Looking for match = {key} : Score {value}")

    print(f'\n{('-_')*50}Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return res.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    

# Main.py
# Testing the response system
while True:
    user_input = input('You: ')
    bot_response = get_response(user_input)

    sentiment = polarity.analyze_sentiment(bot_response)
    current_time = polarity.time_analyze()
    print(f"| Sentiment: {polarity.sentiment} | Time: {current_time} |")
    print(f'Bot: {bot_response}')


    