import configparser

config = configparser.ConfigParser()
config.read("config.ini")

price = 1000
discount = float(config["DISCOUNT"]["rate"]) / 100
tax = float(config["TAX"]["rate"]) / 100

price_after_discount = price - (price * discount)
final_price = price_after_discount + (price_after_discount * tax)

print(final_price)
