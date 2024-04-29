# Grade Score 

Grading essays is a time-consuming task for university professors, often leading to delays in providing feedback to students. Additionally, subjective biases may influence grading consistency. To address these challenges, we aim to develop an automated essay grading system powered by Natural Language Processing (NLP) techniques. This system will enable professors to efficiently assess students' essays, provide timely feedback, and identify areas for improvement, ultimately enhancing the grading process and learning outcomes.

Key features include user authentication to ensure security and privacy, essay submission supporting text or document formats, and rigorous analysis including word count verification, keyword identification, and fact-checking capabilities. Additionally, the system evaluates grammar coherence and vocabulary usage to ensure high-quality assessments. By streamlining the grading process, this system aims to provide timely feedback to students while enhancing grading consistency and ultimately improving learning outcomes.

The application includes the following webpages: Home, About us, Login/register, Contact, Uploading page, Submission page, Grading page (shows grades), Grading report, Get pricing, Terms and Privacy policy, and Careers

NLP Model

The NLP model will test the answer provided by the student using the following criteria: Accuracy, Organization, Grammar, Vocabulary, Punctuation, Relevance, and Coherence.

Methodologies for NLP Model:

* Accuracy: Uses a Hugging Face's pre-trained sentence-transformers model (all-MiniLM-L6-v2) to compute the semantic similarity between two text inputs. It converts the input sentences into 384-dimensional vectors using the model, calculates the cosine similarity between these vectors, and then adjusts this raw similarity score into a percentage format with a non-linear transformation.
* Organization: Uses all-MiniLM-L6-v2 to evaluate the organization quality of a given text by measuring the semantic similarity between consecutive sentences. It first splits the input text into sentences, computes their **pairwise cosine similarities** to generate embeddings, and then averages these similarities to provide an overall organization score expressed as a percentage.
* Relevance: Uses the pre-trained model - 'clips/mfaq' to evaluate the relevance of a student's answer to a specified question to a reference answer. The question, inputted answer, and reference answers are encoded into vector embeddings and their cosine similarities are computed, assessing how closely the student's response aligns with the reference in terms of contextual relevance.
* Coherence: Uses pre-trained model, aisingapore/coherence-momentum to evaluate the coherence of two pieces of text (the reference answer and the student-inputted answer). The texts are preprocessed and converted into tensor formats suitable for the model, then compute a coherence score for each text, returning these scores as an array.
