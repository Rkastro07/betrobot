import json
import requests
from typing import Any, Dict, Optional

def fetch_odds(api_url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Fetch odds from the given API URL.

    Args:
        api_url: Endpoint of the odds API.
        params: Optional query parameters for the API.

    Returns:
        Parsed JSON response from the API.
    """
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """Example usage of :func:`fetch_odds`."""
    api_url = "https://example.com/api/odds"  # Replace with your actual API
    odds = fetch_odds(api_url)
    with open("odds.json", "w") as f:
        json.dump(odds, f, indent=2)
    print("Saved odds to odds.json")


if __name__ == "__main__":
    main()
