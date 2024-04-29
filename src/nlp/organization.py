from sentence_transformers import SentenceTransformer,util
import warnings

def organization(answer):
    #Ignore all warnings
    warnings.filterwarnings('ignore')
    #Split in senteces
    sentence = answer.replace("!",".").replace("?",".").split(".")

    similarity = []
    if len(sentence)>1:
        for i in range(len(sentence)-1):
            #Get Similarity from model for each 2 neighbouring sentences
            similarity.append(A2A(sentence[i],sentence[i+1]))
    else:
        return float(100)
    
    final_similarity = (sum(similarity) / len(similarity) + 1)*50

    if final_similarity < 0:
        final_similarity = 0 

    return final_similarity

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def A2A(ans1,ans2):
    #Importing pre-trained model from hugging face
    
    
    #Converting reference answer to 384 dimensions vectors
    ref_embedding = model.encode(ans1, convert_to_tensor=True)
    ans_embedding = model.encode(ans2, convert_to_tensor=True)
    ans_similarity = float(util.pytorch_cos_sim(ref_embedding, ans_embedding))

    return ans_similarity
