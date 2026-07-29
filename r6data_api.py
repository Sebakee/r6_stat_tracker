import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("R6DATA_API_KEY")


def get_full_stats(
    name: str,
    platform: str = "psn",
    platform_family: str = "console",
    season: str = "all",
    mode: str = "ranked",
    max_retries: int = 5
):
    if not API_KEY:
        raise RuntimeError("Missing R6DATA_API_KEY environment variable")

    url = "https://api.r6data.com/api/stats"

    params = {
        "type": "fullStats",
        "nameOnPlatform": name,
        "platformType": platform,
        "platform_families": platform_family,
        "seasonYear": season,
        "modes": mode,
    }

    headers = {
        "api-key": API_KEY
    }

    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt}/{max_retries}...")

        response = requests.get(url, params=params, headers=headers, timeout=30)
        print("Status code:", response.status_code)

        if response.status_code == 200:
            return response.json()

        try:
            error_data = response.json()
            print(error_data)
            retry_after = int(error_data.get("retryAfter", 10))
        except Exception:
            print(response.text)
            retry_after = 10

        if response.status_code == 503:
            print(f"R6Data is overloaded. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue

        response.raise_for_status()

    raise RuntimeError("R6Data stayed overloaded after all retries. Try again later.")