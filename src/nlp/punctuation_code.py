from deepmultilingualpunctuation import PunctuationModel
import string

model = PunctuationModel()

# Function to count punctuation marks in a text
def count_punctuation(text):
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    return punctuation_count

def puncscore(text):
    corrected_text = model.restore_punctuation(text)
    original_punctuation_count = count_punctuation(text)
    corrected_punctuation_count = count_punctuation(corrected_text)
    if corrected_punctuation_count > 0:
        punctuation_score = original_punctuation_count / corrected_punctuation_count
    else:
        words_in_sentence = len(text.split())
        punctuation_score = original_punctuation_count / words_in_sentence
    return punctuation_score

"""
# Restore punctuation in the text
corrected_text = model.restore_punctuation(text)

# Count punctuation marks in the original and corrected texts
original_punctuation_count = count_punctuation(text)
corrected_punctuation_count = count_punctuation(corrected_text)

# Calculate punctuation score
if corrected_punctuation_count > 0:
    punctuation_score = original_punctuation_count / corrected_punctuation_count
else:
    words_in_sentence = len(text.split())
    punctuation_score = original_punctuation_count / words_in_sentence

print("Original text:", text)
print("Corrected text:", corrected_text)
print("Punctuation score:", punctuation_score)
"""