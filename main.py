from textblob import TextBlob

text = "ENTER_TEXT_HERE"

def Percentage(sentiment):
    
    Number = 0.000
    Numbers = []
    while Number < 1.001:
        Numbers.append(Number)
        Number = Number + 0.001

    NewNumbers = []
    for n in Numbers:
        NewNumbers.append(round(n, 3))

    NewSentiment = round(sentiment, 3)

    Negative = False

    if NewSentiment < 0:
        Negative = True

    if Negative:
        NewSentiment = NewSentiment * -1
        NewSentiment = NewSentiment * 100
        NewSentiment = NewSentiment * -1
        DataReturn = NewSentiment

    if not Negative:
        NewSentiment = NewSentiment * 100
        DataReturn = NewSentiment
    
    return DataReturn

blob = TextBlob(text)

Sentiment = blob.sentiment.polarity 
# Sentiment returns from -1 to +1
# +1 - most positive
# -1 - most negative

Turn_Into_Percentage = Percentage(Sentiment) # Turns sentiment to percentage

print(Turn_Into_Percentage) # print