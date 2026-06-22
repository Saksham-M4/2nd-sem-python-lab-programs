def process_data(data, callback):
    processed_data = [item * 2 for item in data]
    callback(processed_data)

def print_list(data_list):
    print(f"Processed list: {data_list}")

process_data([1, 2, 3], print_list)