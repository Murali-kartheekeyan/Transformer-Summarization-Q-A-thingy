from transformers import pipeline

def load_models():
    print("Loading models... This may take a few minutes.")
    try:
        summarizer = pipeline("summarization", model="nsi319/legal-pegasus")
        question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")
        print("Models loaded successfully!")
        return summarizer, question_answerer
    except Exception as e:
        print(f"Error loading models: {e}")
        print("Please ensure you have a stable internet connection.")
        return None, None