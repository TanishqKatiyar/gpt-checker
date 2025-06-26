import nltk
nltk.download('punkt')  # Ensure punkt is downloaded
from nltk.tokenize import word_tokenize

text = "This is a simple test sentence."
tokens = word_tokenize(text)
print(tokens)
