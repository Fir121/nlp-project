from sentence_transformers import SentenceTransformer,util
import warnings,math

def accuracy(ref_answer,answer):
    #Ignore all warnings
    warnings.filterwarnings('ignore')
    #Get Similarity from model
    similarity = A2A(ref_answer,answer)
    final_similarity = (1 - 1 / math.exp(3*abs(similarity)))*100

    return final_similarity


def A2A(ref_ans,ans):
    #Importing pre-trained model from hugging face
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    #Converting reference answer to 384 dimensions vectors
    ref_embedding = model.encode(ref_ans, convert_to_tensor=True)
    ans_embedding = model.encode(ans, convert_to_tensor=True)
    ans_similarity = float(util.pytorch_cos_sim(ref_embedding, ans_embedding))

    return ans_similarity