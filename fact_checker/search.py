import requests

# Function to get fact-checking information from DuckDuckGo
def get_fact_from_duckduckgo(query: str):
    # A simple request to DuckDuckGo's API for relevant search results
    response = requests.get(f"https://api.duckduckgo.com/", params={
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    })

    if response.status_code == 200:
        data = response.json()
        return {
            "abstract": data.get("Abstract", "No abstract available."),
            "url": data.get("AbstractURL", "No URL available.")
        }
    else:
        return {"error": "Failed to retrieve information from DuckDuckGo"}
