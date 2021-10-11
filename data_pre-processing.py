from typing import List, Text, Tuple
from nltk import stem
import nltk
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

def tagWords(sentences:list) -> List[List[tuple]]:
    """This function tags the each word to its part of speech like Ramish is Noun and Coding is verb"""
    tagged = []
    for sentence in sentences :
        words = nltk.word_tokenize(sentence)
        tagged.append(nltk.pos_tag(words))
    
    return tagged

def chunking_or_chinking(tagged_words:List[List[tuple]], regex:str) -> None:
    """Either sse to group the tagged words on specific parts of speech or remove the words from chunks"""
    chunkGram = regex
    chunkParser = nltk.RegexpParser(chunkGram)

    for tagged_word in tagged_words: 
        chunked = chunkParser.parse(tagged_word)
        chunked.draw()

def entityRecognition(tagged_words:List[List[tuple]], binary=False) -> None:
    """Identify the entity of the word and chunks on that bases like America is Location"""
    for tagged_word in tagged_words:
        namedEntity = nltk.ne_chunk(tagged_word, binary=binary)
        namedEntity.draw()


# print(tokenizing(input_sentence))
# print(stopWords(input_sentence))
# print(stemming(input_sentence))
# print(tagWords(customTokenizer(state_union.raw('2005-GWBush.txt'), state_union.raw('2006-GWBush.txt'))))

# regex_chunk = r"""Chunk: {<NNP.?>*<NN.?>*<VB.?>*}"""
# regex_chink = r"""Chunk: {<.*>+} 
#                             }<VB.?|IN|DT>+{"""
# chunking_or_chinking(tagWords(customTokenizer(state_union.raw('2005-GWBush.txt'), state_union.raw('2006-GWBush.txt'))), regex_chink)

entityRecognition(tagWords(customTokenizer(state_union.raw('2005-GWBush.txt'), state_union.raw('2006-GWBush.txt'))))