from sentence_transformers import SentenceTransformer,util
import warnings

def SemanticSimilarity(question,ref_answer,answers):
    #Ignore all warnings
    warnings.filterwarnings('ignore')
    #Get Similarity from model1
    similarity1 = A2A(ref_answer,answers)
    #Q2A model requires start tags to know which is question and which is answer
    question = "<Q>" + question
    answers = ["<A>" + ans for ans in answers]
    #Get Similarity from model2
    similarity2 = Q2A(question,answers)
    
    A2A_weight = 0.5
    Q2A_weight = 0.5
    final_similarity = [similarity1[i]*A2A_weight+similarity2[i]*Q2A_weight for i in range(len(similarity1))]
    return final_similarity

def Q2A(question,ans_list):
    #Importing pre-trained model from hugging face
    model = SentenceTransformer('clips/mfaq')
    
    #Converting reference answer to 768 dimensions vectors
    question_embedding = model.encode(question, convert_to_tensor=True)
    
    question_relevance = []
    
    #Iterating thorugh all answers, converting to 384 dimension vectors, finding similarity with question
    for i in range(len(ans_list)):
        ans_embedding = model.encode(ans_list[i], convert_to_tensor=True)
        question_relevance.append(float(util.pytorch_cos_sim(question_embedding, ans_embedding)))
    
    return question_relevance

def A2A(ref_ans,ans_list):
    #Importing pre-trained model from hugging face
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    #Converting reference answer to 384 dimensions vectors
    ref_embedding = model.encode(ref_ans, convert_to_tensor=True)
    
    ans_similarity = []

    #Iterating thorugh all answers, converting to 384 dimension vectors, finding similarity with reference
    for i in range(len(ans_list)):
        ans_embedding = model.encode(ans_list[i], convert_to_tensor=True)
        ans_similarity.append(float(util.pytorch_cos_sim(ref_embedding, ans_embedding)))

    return ans_similarity
