import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def calculate_vocabulary_score(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Initialize WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize words, remove stopwords and non-alphanumeric characters
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalnum() and word.lower() not in stopwords.words('english')]

    # Calculate the number of unique words
    unique_words = set(words)

    # Calculate vocabulary score
    if len(words) > 0:
        score = len(unique_words) / len(words)
    else:
        score = 0

    return score

def main():
    # Input text
    text = "rajdeep likes running. He compares running to meditation. It feels melodic and spiritual."

    # Calculate vocabulary score
    score = calculate_vocabulary_score(text)

    # Print the vocabulary score
    print("Vocabulary Score: {:.2f}".format(score))

if __name__ == "__main__":
    main()
