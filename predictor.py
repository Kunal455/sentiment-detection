

import pickle
import re


try:
    with open("go_emotion_model.pkl", "rb") as f:
        model_pipe = pickle.load(f)
    print("GoEmotions model loaded successfully.")
except FileNotFoundError:
    model_pipe = None
    print("Warning: go_emotion_model.pkl not found. Please run train_go_model.py first.")

def clean_text(text):
    
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def predict_emotion(text):
    if model_pipe is None:
        return "Model not loaded ❌"
        
    try:

        pred_label = model_pipe.predict([text])[0]
        
        emojis = {
            'joy': '😊', 'love': '❤️', 'sadness': '😢', 'anger': '😡', 
            'fear': '😨', 'surprise': '😲', 'neutral': '😐', 
            'admiration': '🤩', 'amusement': '😄', 'annoyance': '😒',
            'approval': '👍', 'caring': '🤗', 'confusion': '😕',
            'curiosity': '🤔', 'desire': '😍', 'disappointment': '😞',
            'disapproval': '👎', 'disgust': '🤢', 'embarrassment': '😳',
            'excitement': '😃', 'gratitude': '🙏', 'grief': '😭',
            'nervousness': '😬', 'optimism': '🤞', 'pride': '🦁',
            'realization': '💡', 'relief': '😌', 'remorse': '😔'
        }
        
        emoji = emojis.get(pred_label, '✨')
        return f"{emoji} {pred_label.capitalize()}"
    except Exception as e:
        return f"Error: {e}"
