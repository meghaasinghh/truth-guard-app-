from transformers import pipeline

# Load the model once when the app starts
fact_check_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Function to check if the claim is true or false based on reference
def check_fact(claim: str, reference: str):
    labels = ["true", "false"]  # You can also add "uncertain" if needed
    result = fact_check_model(claim, candidate_labels=labels, hypothesis_template="This claim is {}.")
    
    # Return the most probable label with confidence
    return {
        "is_true": result["labels"][0] == "true",
        "confidence": result["scores"][0],
        "label": result["labels"][0]
    }
