import time

def fetch_data_async(url, callback):
    print(f"Fetching data from {url}...")
    time.sleep(2)

    data = {
        "url": url,
        "content": "Some data from server"
    }

    callback(data)

def handle_fetched_data(data):
    print(f"Data received: {data}")

print("\nStarting async data fetch...")

fetch_data_async(
    "https://api.example.com/data",
    handle_fetched_data
)

print("Async data fetch initiated, continuing with other tasks...")