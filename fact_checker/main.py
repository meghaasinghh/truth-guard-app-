from fastapi import FastAPI
from pydantic import BaseModel
from fact_checker.model import check_fact
from fact_checker.search import get_fact_from_duckduckgo

app = FastAPI()

class FactRequest(BaseModel):
    query: str

@app.post("/fact-check")
async def fact_check(request: FactRequest):
    claim = request.query

    # Get reference fact from DuckDuckGo
    ddg_result = get_fact_from_duckduckgo(claim)
    reference = ddg_result.get("abstract", "")

    # Pass both the claim and reference to the model
    model_result = check_fact(claim, reference)

    return {
        "claim": claim,
        "reference": reference,
        "url": ddg_result.get("url"),
        "model_result": model_result
    }
