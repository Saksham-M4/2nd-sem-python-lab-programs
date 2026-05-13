d = { "name" : "saksham", "age" : 19 , "college" : "GCU"}
for key, value in d.items():
    print(f"key:{key} , value:{value}")

print(d.get("name"))
print(d["name"])
print(d.get("age"))
print(d["age"])
d["city"] = "Bangalore"
print(d["city"])
print("key is :{} , Value is :{}".format(key , value))

    
