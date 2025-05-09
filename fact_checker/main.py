import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from fact_checker.model import check_fact
from fact_checker.search import get_fact_from_duckduckgo
from fact_checker.claim_extractor import extract_claims

app = FastAPI()

class FactRequest(BaseModel):
    query: str  # Full news content or article text

@app.post("/fact-check")
async def fact_check(request: FactRequest):
    # Step 1: Extract individual claims from the query
    claims = extract_claims(request.query)

    results = []

    for claim in claims:
        # Step 2: Get reference fact from DuckDuckGo
        ddg_result = get_fact_from_duckduckgo(claim)
        reference = ddg_result.get("abstract", "")

        # Step 3: Check the claim using your model
        model_result = check_fact(claim, reference)

        # Step 4: Store result
        results.append({
            "claim": claim,
            "reference": reference,
            "url": ddg_result.get("url"),
            "model_result": model_result
        })

    return {"results": results}
