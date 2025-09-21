import random
from nltk.corpus import wordnet

def get_synonym(word: str) -> str:
    """Return a random synonym for a given word if available."""
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    synonyms = list(set(synonyms))
    if synonyms:
        return random.choice(synonyms).replace("_", " ")
    return word

def funny_style(quote: str) -> str:
    words = quote.split()
    return " " + " ".join(get_synonym(w) if random.random() > 0.7 else w for w in words)

def motivational_style(quote: str) -> str:
    return " Remember: " + quote.capitalize() + " Keep going!"

def poetic_style(quote: str) -> str:
    return " " + quote.replace(".", ",") + " ...like a whisper in the wind."
