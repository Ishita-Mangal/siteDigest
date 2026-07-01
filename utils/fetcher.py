import requests


def fetch_website(url):
    try:
        response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    },
    timeout=10
)

        response.raise_for_status()

        return response.text

    except Exception as e:
        raise Exception(f"Failed to fetch website: {str(e)}")
