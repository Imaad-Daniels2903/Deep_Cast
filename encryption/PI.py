import requests

def digits(start: int = 0, num_digits: int = 100) -> str:
    """
    Fetches a specific range of Pi digits from the Pi.delivery API.
    
    :param start: The starting digit index (0 is the initial '3').
    :param num_digits: How many digits to fetch (max 1000 per request).
    :return: A string of the requested Pi digits.
    """
    url = "https://api.pi.delivery/v1/pi"
    params = {
        "start": start,
        "numberOfDigits": num_digits
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes (4ff or 5ff)
        
        data = response.json()
        return data.get("content", "")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return ""