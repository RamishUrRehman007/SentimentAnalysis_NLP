from typing import Text, Tuple
from nltk import stem
from nltk.tokenize import (
                        word_tokenize,
                        sent_tokenize,
                        PunktSentenceTokenizer
                    )
from nltk.corpus import (
                        stopwords,
                        state_union
                    )
from nltk.stem import PorterStemmer

# import nltk
# nltk.download('all')


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

def customTokenizer(training_data:Text, sample_data:Text) -> list:
    """Used to train the tokenizer and build custom model as per our data"""
    custon_sent_tokenizer = PunktSentenceTokenizer(training_data)
    return custon_sent_tokenizer.tokenize(sample_data)



# print(tokenizing(input_sentence))
# print(stopWords(input_sentence))
# print(stemming(input_sentence))
print(customTokenizer(state_union.raw('2005-GWBush.txt'), state_union.raw('2006-GWBush.txt')))

