# polarity.py

from textblob import TextBlob
from datetime import datetime, time
import math

def analyze_sentiment(text):
    # Get the polarity score (-1 to 1)
    # Classify the sentiment based on the polarity
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    return polarity


def time_analyze():
    # Normal time is not multiplied, by sentient analysis. 
    # Get the current time
    current_time = datetime.now().time()


    # Analyze the current time
    if time(0, 0, 0) <= current_time < time(1, 0, 0):
        return 1.9
    elif time(1, 0, 0) <= current_time < time(2, 0, 0):
        return 2.1
    elif time(2, 0, 0) <= current_time < time(3, 0, 0):
        return 2.3
    elif time(3, 0, 0) <= current_time < time(4, 0, 0):
        return 2.4
    elif time(4, 0, 0) <= current_time < time(5, 0, 0):
        return 2.5
    elif time(5, 0, 0) <= current_time < time(6, 0, 0):
        return 2.6
    elif time(6, 0, 0) <= current_time < time(7, 0, 0):
        return 1.3
    elif time(7, 0, 0) <= current_time < time(8, 0, 0):
        return 1.2
    elif time(8, 0, 0) <= current_time < time(9, 0, 0):
        return 0.8
    elif time(9, 0, 0) <= current_time < time(10, 0, 0):
        return 0.9
    elif time(10, 0, 0) <= current_time < time(11, 0, 0):
        return 0.11
    elif time(11, 0, 0) <= current_time < time(12, 0, 0):
        return 0.12
    elif time(12, 0, 0) <= current_time < time(13, 0, 0):
        return 0.13
    elif time(13, 0, 0) <= current_time < time(14, 0, 0):
        return 0.14
    elif time(14, 0, 0) <= current_time < time(15, 0, 0):
        return 0.15
    elif time(15, 0, 0) <= current_time < time(16, 0, 0):
        return 0.16
    elif time(16, 0, 0) <= current_time < time(17, 0, 0):
        return 0.17
    elif time(17, 0, 0) <= current_time < time(18, 0, 0):
        return 0.18
    elif time(18, 0, 0) <= current_time < time(19, 0, 0):
        return 0.19
    elif time(19, 0, 0) <= current_time < time(20, 0, 0):
        return 0.21
    elif time(20, 0, 0) <= current_time < time(21, 0, 0):
        return 0.22
    elif time(21, 0, 0) <= current_time < time(22, 0, 0):
        return 1.3
    elif time(22, 0, 0) <= current_time < time(23, 0, 0):
        return 1.4
    elif time(23, 0, 0) <= current_time < time(0, 0, 0):
        return 1.5
    else:
        result = f"Not Normal (x) = {str(current_time)}"
        return result


# Example usage
text_to_analyze = "i hate"
#text_to_analyze = "I hate using TextBlob. It's bad!"

# Call the functions
sentiment = analyze_sentiment(text_to_analyze)
current_time_result = time_analyze()


# Add the sentiment score and the time analysis result
if -1 <= sentiment < 0:
    result_sum = (sentiment - 0.5 * math.sin(2 * math.pi * (current_time_result / 24)))

if 0 <= sentiment <= 1:
    result_sum = (sentiment + 0.5 * math.sin(2 * math.pi * (current_time_result / 24)))         

# Print the results
print(f"SENTIMENT: {sentiment}")
print("TIME: ", datetime.now().time()," : " ,current_time_result)
print("SUM: ", result_sum)


# TIME: 01:12:22.491632, original value SENTIENT: -0.8374999999999999, Change = -0.9374999999999999
# TIME: 01:12:22.491632, original value SENTIENT: 0.8374999999999999, Change = 0.7374999999999999
# TIME: 10:12:22.491632, original value SENTIENT: -0.8374999999999999, Change = -0.7374999999999999
# TIME: 10:12:22.491632, original value SENTIENT: 0.8374999999999999, Change = 0.9374999999999999

# T = I HATE
# SENTIMENT: -0.8374999999999999
# TIME: 13:28:37.659644
# SUM: -0.7463822372539262

# T = I LOVE
# SENTIMENT: 0.75
# TIME: 13:29:49.722979
# SUM: 0.8411177627460737
