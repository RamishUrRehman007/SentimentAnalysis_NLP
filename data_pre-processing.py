from typing import Text, Tuple
from nltk import stem
from nltk.tokenize import (
                        word_tokenize,
                        sent_tokenize
                    )
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk
# nltk.download('popular')


input_sentence = "Hello, I am Ramish. You can call me python maniac or pythonic or pythoner or the learner. I love to work with AI, Cybersecuirty, REST and cloud"

def tokenizing(input_sentence:str) -> Tuple[list]:
    """Tokenize the paragraph into the word and sentence list"""
    return word_tokenize(input_sentence), sent_tokenize(input_sentence)

def stopWords(input_sentence:str) -> list:
    """Remove the stopwords or neutral words from the paragraph"""
    input_sentence = word_tokenize(input_sentence)
    stop_words = set(stopwords.words("english"))
    return [i for i in input_sentence if i.lower() not in stop_words]

def stemming(input_sentence:str) -> list:
    """Basically its find the root of the word(normalization) for example the root of writing, written, write is write"""
    ps = PorterStemmer()
    return [ps.stem(w) for w in word_tokenize(input_sentence)]



print(tokenizing(input_sentence))
print(stopWords(input_sentence))
print(stemming(input_sentence))

