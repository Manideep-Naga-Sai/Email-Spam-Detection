import re
from nltk.corpus import stopwords

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)

    words = text.split()

    words = [word for word in words
             if word not in stopwords.words('english')]

    return " ".join(words)
