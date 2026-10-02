

import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# --- Console handler (with line numbers) ---
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
console_handler.setFormatter(console_formatter)

# --- File handler (without line numbers) ---
file_handler = logging.FileHandler("project.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example log
logger.info("This message shows line number in terminal only")











length_of_land = 100
breadth_of_land = 100
bricks_cost_per_price = 10.5
labour_mistri1 = "saksham"
labour_mistri2 = "rahul"
is_home = True 

# calculate the area and perimeter
total_area_of_land = length_of_land * breadth_of_land
perimeter_of_land = 2 * (length_of_land + breadth_of_land)

logging.info(f"Total area of land is {total_area_of_land} square ft")
logger.info(f"Perimeter of land is {perimeter_of_land} ft")

length_of_land = int(input("Please enter your length of your land:"))
breadth_of_land = input("Please enter your breadth of your land:")
total_area_of_your_land = length_of_land  * float (breadth_of_land)
logger.info(f"Total area of your land is {total_area_of_your_land} square ft")
