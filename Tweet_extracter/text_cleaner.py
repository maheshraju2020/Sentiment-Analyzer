import string
from stopwords import stopwords


class cleaner:
    def __init__(self):
        self.stop_words = stopwords
        self.punctuation = string.punctuation

    def lower(self, text):
        """
        Makes the text lowercase
        """
        return text.lower()

    def remove_punctuation(self, text):
        """
        Removes the punctuations from the text
        """
        new_text = ""
        for i in text:
            if i not in self.punctuation:
                new_text += i
        return new_text

    def remove_hashtag(self, text):
        """
        Removes the hashtag from the text
        """
        new_text = ""
        for i in text:
            if i != "#":
                new_text += i
        return new_text

    def tokenize(self, text):
        """
        tokenize the tweets
        """
        return text.split()

    def getAplhaTokens(self, tokens):
        """
        Removes the non alphabetic tokens
        """
        return [token for token in tokens if token.isalpha()]

    def remove_stopwords(self, tokens):
        """
        Removes the stopwords for the text
        """
        return [token for token in tokens if token not in self.stop_words]

    def combine_tokens(self, tokens):
        """
        Combines the tokens, to form a string
        """
        return " ".join(tokens)

    @staticmethod
    def linkChecker(text):
        if "http://" in text or "https://" in text:
            return True
        else:
            return False

    def clean_text(self, text):
        text = self.lower(text)
        text = self.remove_punctuation(text)
        text = self.remove_hashtag(text)
        tokens = self.tokenize(text)
        tokens = self.getAplhaTokens(tokens)
        tokens = self.remove_stopwords(tokens)
        text = self.combine_tokens(tokens)
        return text
