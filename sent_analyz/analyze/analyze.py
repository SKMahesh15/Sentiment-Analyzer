from collections import Counter
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt

class SentimentAnalyzer:
    def __init__(self):
        self.final_words = []
        self.emotions_list = []
        self.neg = 0
        self.neu = 0
        self.pos = 0
        
    def lower_case(self):
        lower = self.text.lower()
        self.final_text = lower.translate(str.maketrans('', '', string.punctuation))
        return self.final_text

    def tokenize_word(self):
        self.tokenized_word = word_tokenize(self.final_text)
        for word in self.tokenized_word:
            if word not in stopwords.words('english'):
                self.final_words.append(word)
        return self.final_words

    def emotional_words(self):
        with open('emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(',', '').replace("'", '').strip()
                word, emotion = clear_line.split(':')
                # print(f"Word:{word} Emotion:{emotion}")

                if word in self.final_words:
                    self.emotions_list.append(emotion)
    
    def sentiment_analyze(self):
        analyser = SentimentIntensityAnalyzer().polarity_scores(self.final_text)
        if analyser['neg'] > analyser['pos']:
            self.neg += 1
        elif analyser['pos'] > analyser['neg']:
            self.pos += 1
        else:
            self.neu += 1

    def analyze(self, text):
        for x in text:
            self.text = x
            self.lower_case()
            self.tokenize_word()
            self.emotional_words()
            self.sentiment_analyze()
            
        return [self.neg, self.neu, self.pos]
        
if __name__ == '__main__':
    sa = SentimentAnalyzer()
    sa.analyze(["really good", "bad"])