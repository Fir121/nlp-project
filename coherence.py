from sgnlp.models.coherence_momentum import CoherenceMomentumModel,CoherenceMomentumConfig,CoherenceMomentumPreprocessor
import warnings

def coherence(ref_ans,ans):
    #Ignore all warnings
    warnings.filterwarnings('ignore')

    """config = CoherenceMomentumConfig.from_pretrained(
        "https://storage.googleapis.com/sgnlp-models/models/coherence_momentum/config.json")
    model = CoherenceMomentumModel.from_pretrained(
        "https://storage.googleapis.com/sgnlp-models/models/coherence_momentum/pytorch_model.bin",
        config=config)
        
        model.save_pretrained("coherence_model")
        """
    
    config = CoherenceMomentumConfig.from_pretrained("coherence_model")
    model = CoherenceMomentumModel.from_pretrained("coherence_model")
    
    preprocessor = CoherenceMomentumPreprocessor(config.model_size, config.max_len)
    text1_tensor = preprocessor([ref_ans])
    text2_tensor = preprocessor([ans])

    text1_score = model.get_main_score(text1_tensor["tokenized_texts"]).item()
    text2_score = model.get_main_score(text2_tensor["tokenized_texts"]).item()

    return [text1_score,text2_score]

