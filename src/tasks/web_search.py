import requests

def web_search(query):
    url = f"https://api.example.com/search?q={query}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    query = "Sample search query"
    results = web_search(query)
    print(results)
