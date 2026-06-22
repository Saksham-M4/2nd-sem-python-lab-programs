class Button:

    def __init__(self, name):
        self.name = name
        self.on_click = None

    def click(self):
        if self.on_click:
            self.on_click(self.name)

def button_handler(button_name):
    print(f"{button_name} button was clicked!")

my_button = Button("Submit")
my_button.on_click = button_handler
my_button.click()