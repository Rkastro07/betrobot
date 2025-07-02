"""Fetch and store betting odds from a remote API."""

import argparse
import json
import os
from typing import Any, Dict, Optional

import requests

def fetch_odds(
    api_url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Fetch odds from the given API URL.

    Args:
        api_url: Endpoint of the odds API.
        params: Optional query parameters for the API.
        headers: Optional headers to send with the request (e.g. authentication).

    Returns:
        Parsed JSON response from the API.
    """
    response = requests.get(api_url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """Fetch odds from an API and save the result to ``odds.json``."""

    parser = argparse.ArgumentParser(description="Update odds from a remote API")
    parser.add_argument(
        "--url",
        default=os.getenv("ODDS_API_URL", "https://example.com/api/odds"),
        help="Endpoint of the odds API",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="Query parameter in the form key=value. Can be used multiple times.",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("ODDS_API_TOKEN"),
        help="Bearer token for Authorization header",
    )
    args = parser.parse_args()

    params = dict(p.split("=", 1) for p in args.param if "=" in p) or None
    headers = {"Authorization": f"Bearer {args.token}"} if args.token else None

    odds = fetch_odds(args.url, params=params, headers=headers)
    with open("odds.json", "w") as f:
        json.dump(odds, f, indent=2)
    print("Saved odds to odds.json")


if __name__ == "__main__":
    main()
