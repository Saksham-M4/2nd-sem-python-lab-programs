from loguru import logger

labour_with_cost = {
    "manu": 500,
  "kg": 400,
    "vk": 300
}

labour_with_cost["virat"] = 900
labour_with_cost["saksham"] = 800  

logger.info(labour_with_cost.keys())
logger.info(labour_with_cost.values())
logger.info(labour_with_cost["saksham"])
for i in labour_with_cost:
    print(i , labour_with_cost[i])
 
 


for key, value in labour_with_cost.items():
 logger.info(" {} {}".format(key, value))
 data = {
    "MAINDATA": [
        {"IDD": "A1"},
        {"IDD": "B2"},
        {"IDD": "C3"}
    ]
}
for i in range(len(data["MAINDATA"])):
    print(data["MAINDATA"][i]["IDD"])


data = {
    "MAINDATA": [
        {
            "IDD": "A1",
            "HeaderFields": [
                {"FieldTypeName": "H11", "Value": "100"},
                {"FieldTypeName": "H12", "Value": "200"}
            ]
        }
    ]
}
print(data["MAINDATA"][0]["HeaderFields"])
for h in data["MAINDATA"][0]["HeaderFields"]:
    print(h["FieldTypeName"], h["Value"])
data = {
    "MAINDATA": [
        {"IDD": "A1"},
        {"IDD": "B2"}
    ]
}
for item in data["MAINDATA"]:
    if item["IDD"] == "B2":
        print(item["IDD"], "→ MATCH")
    else:
        print(item["IDD"], "→ NOT MATCH")














