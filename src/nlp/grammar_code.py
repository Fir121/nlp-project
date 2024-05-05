from happytransformer import HappyTextToText
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
import nltk 
nltk.download('punkt')
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize

def calculate_grammar_score(input_text, corrected_text):
    # Tokenize input and corrected text
    input_tokens = word_tokenize(input_text.lower())
    corrected_tokens = word_tokenize(corrected_text.lower())

    # Calculate BLEU score to measure similarity
    bleu_score = sentence_bleu([input_tokens], corrected_tokens)

    # Invert BLEU score to get a higher score for more grammatically correct sentences
    grammar_score = 1 - bleu_score

    return grammar_score
