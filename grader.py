import accuracy, relevance, organization, punctuation_code, spelling_code, vocabulary_code, grammar_code


def grader(question,ref_ans,answer):
    final = dict(accuracy = accuracy.accuracy(ref_ans,answer),
                 relevance = relevance.relevance(question,ref_ans,answer),
                 organization = organization.organization(answer),
                 punctuation = punctuation_code.count_punctuation(answer),
                 grammar = grammar_code.calculate_grammar_score(answer, ref_ans),
                 spelling = spelling_code.calculate_spelling_score(answer),
                 vocabulary = vocabulary_code.calculate_vocabulary_score(answer)
                 )
    return final


#Testset

'''question = "How many models can I host on HuggingFace?"
answer_1 = "All plans come with unlimited private models and datasets."
answer_2 = "AutoNLP is an automatic way to train and deploy state-of-the-art NLP models, seamlessly integrated with the Hugging Face ecosystem."
answer_3 = "Based on how much training data and model variants are created, we send you a compute cost and payment link - as low as $10 per job."
grader(question,"infinte",[answer_1,answer_2,answer_3])'''