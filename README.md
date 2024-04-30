# Grade Score 

Grading essays is a time-consuming task for university professors, often leading to delays in providing feedback to students. Additionally, subjective biases may influence grading consistency. To address these challenges, we aim to develop an automated essay grading system powered by Natural Language Processing (NLP) techniques. This system will enable professors to efficiently assess students' essays, provide timely feedback, and identify areas for improvement, ultimately enhancing the grading process and learning outcomes.

Key features include user authentication to ensure security and privacy, essay submission supporting text or document formats, and rigorous analysis including word count verification, keyword identification, and fact-checking capabilities. Additionally, the system evaluates grammar coherence and vocabulary usage to ensure high-quality assessments. By streamlining the grading process, this system aims to provide timely feedback to students while enhancing grading consistency and ultimately improving learning outcomes.

The application includes the following webpages: Home, About us, Login/register, Contact, Uploading page, Submission page, Grading page (shows grades), Grading report, Get pricing, Terms and Privacy policy, and Careers

# Purpose of the Project

Primary: To streamline the essay grading process for university professors while ensuring fairness, consistency, and prompt feedback for students.

* To develop an automated grading system, reducing the time and effort required for essay assessment.
* Implement NLP algorithms to accurately analyze the content, structure, and coherence of essays.
* Provide timely feedback to students to facilitate their learning process.
* Minimize subjective biases in grading by employing objective NLP-based evaluation techniques.
* Design an intuitive and user-friendly interface for professors to interact with the grading system.

# Evaluation Criteria

The NLP model will test the answer provided by the student using the following criteria: Accuracy, Organization, Grammar, Vocabulary, Punctuation, Relevance, and Coherence.

Methodologies for Evaluation Criteria:

* Accuracy: Uses a Hugging Face's pre-trained sentence-transformers model (all-MiniLM-L6-v2) to compute the semantic similarity between two text inputs. It converts the input sentences into 384-dimensional vectors using the model, calculates the cosine similarity between these vectors, and then adjusts this raw similarity score into a percentage format with a non-linear transformation.
* Organization: Uses all-MiniLM-L6-v2 to evaluate the organization quality of a given text by measuring the semantic similarity between consecutive sentences. It first splits the input text into sentences, computes their **pairwise cosine similarities** to generate embeddings, and then averages these similarities to provide an overall organization score expressed as a percentage.
* Grammar: Employs the HappyTransformer and nltk libraries for grammar correction and evaluation. It initializes a HappyTextToText model specifically tuned for grammar correction using a T5 transformer model (vennify/t5-base-grammar-correction). The code also uses NLTK's punkt tokenizer to tokenize text and computes the BLEU score to assess the grammatical accuracy of the corrected text.
* Vocabulary: Uses the NLTK library to evaluate the vocabulary richness of a given text. It starts by tokenizing the text, then lemmatizes each word to its base form using WordNetLemmatizer, and removes common stopwords as well as non-alphanumeric words. The vocabulary score is calculated as the ratio of unique words to the total number of words after processing, providing a measure of the text's lexical diversity.
* Punctuation: Utilizes the deepmultilingualpunctuation library to restore punctuation in text and calculate a punctuation score to evaluate how well the original text matches the punctuation-restored text. A function is defined to count punctuation marks using Python's string.punctuation. It then calculates a punctuation score based on the ratio of original punctuation count to corrected punctuation count. If no punctuation is restored, the score is adjusted based on the number of words in the sentence.
* Relevance: Uses the pre-trained model - 'clips/mfaq' to evaluate the relevance of a student's answer to a specified question to a reference answer. The question, inputted answer, and reference answers are encoded into vector embeddings and their cosine similarities are computed, assessing how closely the student's response aligns with the reference in terms of contextual relevance.
* Coherence: Uses pre-trained model, aisingapore/coherence-momentum to evaluate the coherence of two pieces of text (the reference answer and the student-inputted answer). The texts are preprocessed and converted into tensor formats suitable for the model, then compute a coherence score for each text, returning these scores as an array.

# Tech Stack 

Backend
* Framework: Django - for built-in authentication and ORM capabilities
* Database: MySQL - for storing user authentication data and essay grading information
  
Frontend
* JavaScript Framework: React - for building dynamic user interfaces
* CSS Framework: Bootstrap - for styling and layout
  
Version Control
* GitHub - for collaborative development, version control, and code review

Infrastructure Provisioning and Configuration
* Ansible - for provisioning and configuring infrastructure
  
Testing
* Backend Testing: Python's unit test framework for unit testing.
* Frontend Testing: Selenium WebDriver for automated UI testing.
