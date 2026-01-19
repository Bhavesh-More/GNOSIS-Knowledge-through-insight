import requests

# Load prompt template
with open("ai/prompts/queryTransformer.txt", "r", encoding="utf-8") as file:
    PROMPT_TEMPLATE = file.read()

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"


def transformQuery(user_query: str):
    """
    user_query: raw user input string
    returns: rewritten search-optimized query string
    """

    # Inject user query into prompt
    prompt = PROMPT_TEMPLATE.replace("{user_query}", user_query)

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()

    data = response.json()

    rewritten = data["response"].strip()

    # Fallback safety
    if not rewritten:
        return user_query

    return rewritten
