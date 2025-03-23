import requests
import string
from collections import deque

def fetch_names(prefix):
    """Fetch autocomplete suggestions for a given prefix."""
    url = "http://35.200.185.69:8000/v1/autocomplete"
    params = {"query": prefix}  # Adjust if needed based on API behavior
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()  # Assuming API returns JSON
    except requests.RequestException as e:
        print(f"Error fetching {prefix}: {e}")
        return []

def extract_all_names():
    """Extract all possible names from the autocomplete system."""
    discovered_names = set()
    queue = deque(string.ascii_lowercase)  # Start with all lowercase letters

    while queue:
        prefix = queue.popleft()
        suggestions = fetch_names(prefix)

        for name in suggestions:
            if name not in discovered_names:
                discovered_names.add(name)
                if len(name) > len(prefix):
                    queue.append(name)

    return sorted(discovered_names)

if __name__ == "__main__":
    all_names = extract_all_names()
    print("Extracted Names:", all_names)
