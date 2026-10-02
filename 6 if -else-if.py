from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_price = 10.5
labour_mistri1 = "saksham"
labour_mistri2 = "rahul"
is_home = True 

length_of_land = int(input( "Enter your length of your land:"))
if length_of_land < 100:
    logger.info("length of land is small for 4 bhk")
    logger.info("second line")
    if length_of_land > 80:
        logger.info(" you can build 1 bhk")
    else:
        logger.info(" you can build 2 bhk")
elif length_of_land >= 500:
    logger.info(" you can build 4 bhk")

else:
    logger.info("length of land is sufficient for 4 bhk")
    logger.info("third line")




                           