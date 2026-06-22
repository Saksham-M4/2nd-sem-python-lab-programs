def greet(name, callback):
    message = f"Hello, {name}!"
    callback(message)

def display_message(msg):
    print(msg)

greet("Alice", display_message)