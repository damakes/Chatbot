# Chat-Project
On ongoing project focused on context-aware responses.
The chatbot analyzes user messages, sentiment scores, considers the time of day, and generates responses based on predefined triggers. Sentiment analysis calculates polarity scores, and time analysis adjusts sentiment scores based on the time of day.

Example 1

    "I love using hat. It's warm!"
    SENTIMENT: 0.625
    TIME:  17:30:54.395115 
    SUM:  0.6485532253548213    
Example 2

    "I hate using hat. It's bad!"
    SENTIMENT: -0.8374999999999999
    TIME:  17:31:21.872638 
    SUM:  -0.8610532253548212 
Formula: 

    Result = (sentiment + 0.5 * math.sin(2 * math.pi * (current_time_result / 24)))   

The objective is to utilize the resulting sentiment score for generating responses that are more context-aware. The project is still in progress and not yet ready.
