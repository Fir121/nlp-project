import nlp.accuracy as accuracy
import nlp.relevance as relevance
import nlp.organization as organization
import nlp.punctuation_code as punctuation_code
import nlp.grammar_code as grammar_code
import nlp.spelling_code as spelling_code
import nlp.vocabulary_code as vocabulary_code
import uuid

def generate_html_page(score):
    fpath = f"{uuid.uuid4()}.html"

    fstr = f"<tr><td>{score['accuracy']}</td><td>{score['organization']}</td><td>{score['grammar']}</td><td>{score['vocabulary']}</td><td>{score['punctuation']}</td><td>{score['relevance']}</td><td>{score['spelling']}</td><td>{score['Final Grade']}</td></tr>"

    with open("static/data/"+fpath, 'w') as file:
        file.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Evaluation Report</title><style>table {font-family: Arial, sans-serif;border-collapse: collapse;width: 100%;} th, td {border: 1px solid #dddddd;text-align: left;padding: 8px;} th {background-color: #f2f2f2;}</style></head><body><h2>Evaluation Report</h2><table><thead><tr><th>Accuracy</th><th>organization</th><th>Grammar</th><th>Vocabulary</th><th>Punctuation</th><th>Relevance</th><th>Spelling</th><th>Final Grade</th></tr></thead><tbody>'
                     + fstr                 
                     + "</tbody></table></body></html>"
                     )
    
    return fpath

def grader(question,ref_ans,answer, score):
    final = dict(accuracy = accuracy.accuracy(ref_ans,answer, 1),
                 relevance = relevance.relevance(question,ref_ans,answer),
                 organization = organization.organization(answer),
                 punctuation = punctuation_code.puncscore(answer)*100,
                 grammar = grammar_code.calculate_grammar_score(answer, ref_ans)*100,
                 spelling = spelling_code.calculate_spelling_score(answer)*100,
                 vocabulary = vocabulary_code.calculate_vocabulary_score(answer)*100
                 )
    final["Final Grade"] = sum(final.values())/7
    for key in final:
        final[key] = round((final[key]/100)*score,2)
    final["Max Score"] = score
    print(final)
    path = generate_html_page(final)
    print(path)
    return final

if __name__ == "__main__":
    question = "What is the capital of India?"
    ref_ans = "The capital of India is New Delhi."
    answer = "The capital of India is Rajasthan."
    score = 10
    print(grader(question,ref_ans,answer, score))