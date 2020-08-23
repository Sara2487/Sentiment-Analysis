from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__)

def sentiment_scores(sentence):

    print(sentence)
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict['compound'] >= 0.05:
        return "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        return "Negative"

    else:
        return "Neutral"


@app.route('/')
def submit():
    return render_template('submit.html')

@app.route('/sentiment', methods = ['POST'])
def sentiment():
    sentence = request.form.get('sentence')
    Sentiment = sentiment_scores(sentence)
    return render_template('sentiment.html', sentence= sentence, Sentiment = Sentiment)



if __name__ == '__main__':
    app.run(debug=True)

