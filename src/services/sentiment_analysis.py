from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

from nltk.tokenize import sent_tokenize

def analyze_sentiment(text: str):
    sid = SentimentIntensityAnalyzer()
    sentences = sent_tokenize(text)

    sentence_sentiments = []
    total_compound = 0

    for sent in sentences:
        score = sid.polarity_scores(sent)
        total_compound += score['compound']
        sentiment = "Positive" if score['compound'] >= 0.05 else "Negative" if score['compound'] <= -0.05 else "Neutral"
        sentence_sentiments.append({
            "sentence": sent,
            "compound": score['compound'],
            "sentiment": sentiment
        })

    avg_compound = total_compound / len(sentences)
    overall = "Positive" if avg_compound >= 0.05 else "Negative" if avg_compound <= -0.05 else "Neutral"

    return overall, sentence_sentiments
