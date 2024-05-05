import accuracy, relevance, organization, punctuation_code, spelling_code, vocabulary_code, grammar_code

file_html = open("result.html", "w")
def grader(question,ref_ans,answer,model):
    final = dict(accuracy = accuracy.accuracy(ref_ans,answer,model),
                 relevance = relevance.relevance(question,ref_ans,answer),
                 organization = organization.organization(answer),
                 punctuation = punctuation_code.count_punctuation(answer),
                 grammar = grammar_code.calculate_grammar_score(answer, ref_ans),
                 spelling = spelling_code.calculate_spelling_score(answer),
                 vocabulary = vocabulary_code.calculate_vocabulary_score(answer)
                 )
    return final


def generate_html_page(essays):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Evaluation Report</title>
        <style>
            table {
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Evaluation Report</h2>
        <table>
            <thead>
                <tr>
                    <th>Essay Name</th>
                    <th>Essay ID</th>
                    <th>Student Name</th>
                    <th>School Name</th>
                    <th>Teacher Name</th>
                    <th>Classroom ID</th>
                    <th>Student ID</th>
                    <th>Accuracy</th>
                    <th>organization</th>
                    <th>Grammar</th>
                    <th>Vocabulary</th>
                    <th>Punctuation</th>
                    <th>Relevance</th>
                    <th>Final Grade</th>
                    <th>Remark</th>
                </tr>
            </thead>
            <tbody>
    """

    for essay in essays:
        html_content += """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
        """.format(essay['essay_name'], essay['essay_id'], essay['student_name'], essay['school_name'],
                   essay['teacher_name'], essay['classroom_id'], essay['student_id'], essay['accuracy'],
                   essay['organization'], essay['grammar'], essay['vocabulary'], essay['punctuation'],
                   essay['relevance'], essay['final_grade'], essay['remark'])

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html_content

final = grader("How many models can I host on HuggingFace?","You can host infinite amounts of plans","All plans come with unlimited private models and datasets.")
#Testset
print(final)
sum = float(final['accuracy'])+float(final['relevance'])+float(final['organization'])
result = (sum/3)
# Example usage:
essays = [
    {
        'essay_name': 'Sample Essay',
        'essay_id': '001',
        'student_name': 'John Doe',
        'school_name': 'XYZ High School',
        'teacher_name': 'Ms. Smith',
        'classroom_id': 'Class A',
        'student_id': '123',
        'accuracy': float(final['accuracy']),
        'organization': float(final['organization']),
        'grammar': int(final['grammar']),
        'vocabulary': int(final['vocabulary']),
        'punctuation': int(final['punctuation']),
        'spelling': final['spelling'],
        'relevance': float(final['relevance']),
        'final_grade': result,
        'remark': 'Well done!'
    },
]

html_page = generate_html_page(essays)
file_html.write(html_page)
file_html.close()


'''question = "How many models can I host on HuggingFace?"
answer_1 = "All plans come with unlimited private models and datasets."
answer_2 = "AutoNLP is an automatic way to train and deploy state-of-the-art NLP models, seamlessly integrated with the Hugging Face ecosystem."
answer_3 = "Based on how much training data and model variants are created, we send you a compute cost and payment link - as low as $10 per job."
grader(question,"infinte",[answer_1,answer_2,answer_3])'''