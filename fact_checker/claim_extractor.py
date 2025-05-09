
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download punkt tokenizer once
nltk.download('punkt')

# Extract factual-sounding statements (simple version)
def extract_claims(text: str):
    sentences = sent_tokenize(text)
    
    # Filter sentences that are likely to be factual (heuristic)
    factual_keywords = ["is", "are", "was", "were", "has", "have", "had", "will", "can", "could", "may"]
    claims = [s for s in sentences if any(word in s.lower() for word in factual_keywords)]

    return claims
