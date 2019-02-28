__author__ = 'Akash__rana'
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def primary(sentence):
    score = analyser.polarity_scores(sentence)
    return [['Sentence', 'Sentiment'],['Neutral', score['neu']],['Positive',score['pos']],['Negative',score['neg']]]