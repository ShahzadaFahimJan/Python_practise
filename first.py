import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Fahim loves programming in Python."
words = word_tokenize(text)

# POS Tagging
pos_tags = pos_tag(words)
print(pos_tags)
