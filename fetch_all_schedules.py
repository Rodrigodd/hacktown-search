import requests
import time

API_URL = "https://hacktown-2025-ss-v2.api.yazo.com.br/public/schedules"
PAGE_SIZE = 10  # As per 'per_page' in the JSON
MAX_RETRIES = 3
RETRY_SLEEP = 2  # seconds

def fetch_page(page):
    tries = 0
    while tries < MAX_RETRIES:
        try:
            response = requests.get(API_URL, params={'page': page}, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            tries += 1
            print(f"Error fetching page {page}: {e}. Retry {tries}/{MAX_RETRIES}")
            time.sleep(RETRY_SLEEP)
    return None

def fetch_all_schedules():
    # Fetch the first page to determine total pages
    first_page = fetch_page(1)
    if not first_page:
        print("Failed to fetch first page.")
        return []

    total = first_page['meta']['total']
    per_page = first_page['meta']['per_page']
    last_page = first_page['meta']['last_page']

    print(f"Total events: {total}, per page: {per_page}, total pages: {last_page}")

    all_data = []
    for page in range(1, last_page + 1):
        data = fetch_page(page)
        if data and 'data' in data:
            all_data.extend(data['data'])
            print(f"Fetched page {page}/{last_page} ({len(data['data'])} items)")
        else:
            print(f"Failed to fetch data for page {page}")
    print(f"Fetched total {len(all_data)} events")
    return all_data

if __name__ == "__main__":
    schedules = fetch_all_schedules()
    # Example: Save to file as JSON
    import json
    with open("all_schedules.json", "w", encoding="utf-8") as f:
        json.dump(schedules, f, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    print("All schedules saved to all_schedules.json")
