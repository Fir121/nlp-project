from sentence_transformers import SentenceTransformer,util
import warnings,math

def relevance(question,ref_answer,answer):
    #Ignore all warnings
    warnings.filterwarnings('ignore')
    #Q2A model requires start tags to know which is question and which is answer
    question = "<Q>" + question
    ref_answer = "<A>"+ref_answer
    answer = "<A>" + answer
    #Get Similarity from model
    original_similarity = Q2A(question,ref_answer)
    similarity = Q2A(question,answer)
    final_similarity = (1 / math.exp(15*abs(original_similarity-similarity)))*100

    return final_similarity

def Q2A(question,ans):
    #Importing pre-trained model from hugging face
    model = SentenceTransformer('clips/mfaq')
    
    #Converting reference answer to 768 dimensions vectors
    question_embedding = model.encode(question, convert_to_tensor=True)
    ans_embedding = model.encode(ans, convert_to_tensor=True)
    question_relevance = float(util.pytorch_cos_sim(question_embedding, ans_embedding))
    
    return question_relevance

