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
    html_content = '<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Evaluation Report</title>    <style>        table {            font-family: Arial, sans-serif;            border-collapse: collapse;            width: 100%;        }                th, td {            border: 1px solid #dddddd;            text-align: left;            padding: 8px;        }                th {            background-color: #f2f2f2;        }    </style></head><body>    <h2>Evaluation Report</h2>    <table>        <thead>            <tr>                <th>Accuracy</th>                <th>organization</th>                <th>Grammar</th>                <th>Vocabulary</th>                <th>Punctuation</th>                <th>Relevance</th>                <th>Final Grade</th>                <th>Remark</th>            </tr>        </thead>        <tbody>'

    html_content += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(score['accuracy'], score['organization'], score['grammar'], score['vocabulary'], score['punctuation'],score['relevance'], score['final_grade'], score['remark'])

    html_content += "</tbody></table></body></html>"

    with open("static/data/"+fpath, 'w') as file:
        file.write(html_content)
    
    return fpath

def grader(question,ref_ans,answer):
    final = dict(accuracy = accuracy.accuracy(ref_ans,answer),
                 relevance = relevance.relevance(question,ref_ans,answer),
                 organization = organization.organization(answer),
                 punctuation = punctuation_code.puncscore(answer)*100,
                 grammar = grammar_code.calculate_grammar_score(answer, ref_ans)*100,
                 spelling = spelling_code.calculate_spelling_score(answer)*100,
                 vocabulary = vocabulary_code.calculate_vocabulary_score(answer)*100
                 )
    for key in final:
        final[key] = round(final[key],2)
    print(final)
    path = generate_html_page(final)
    return path, round(sum(final.values())/7, 2)