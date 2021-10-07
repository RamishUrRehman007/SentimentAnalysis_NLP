from nltk.tokenize import (
                        word_tokenize,
                        sent_tokenize
                    )
# import nltk
# nltk.download('popular')

input_sentence = "Hello, I am Ramish. You can call me python maniac or the learner. I love to work with AI, Cybersecuirty, REST and cloud"

print(word_tokenize(input_sentence))
print(sent_tokenize(input_sentence))