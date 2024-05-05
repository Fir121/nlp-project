from textblob import Word
import re

def calculate_spelling_score(sentence):
    words = sentence.split()
    words = [word.lower() for word in words]
    words = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words]
    
    total_score = 0
    misspelled_words = []
    
    for word in words:
        word_obj = Word(word)
        result = word_obj.spellcheck()
        if word == result[0][0]:
            total_score += 1  # Positive contribution for correctly spelled words
        else:
            total_score -= 1  # Negative contribution for misspelled words
            misspelled_words.append((word, result[0][0]))
    
    # Normalize score between 0 and 1
    spelling_score = max(total_score, 0) / len(words) if len(words) > 0 else 0
    
    return spelling_score, misspelled_words

sentence = 'This is a sentencee to check!'
score, misspelled_words = calculate_spelling_score(sentence)

print("Spelling Score:", score)
print("Misspelled Words:")
for word, correction in misspelled_words:
    print(f"    '{word}' should be '{correction}'")
