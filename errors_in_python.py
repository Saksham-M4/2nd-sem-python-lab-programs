
# try:
#     print("Start")
#     print(10 + '5')   # TypeError
# except TypeError as e:
#     print("Type problem happened")
#     print(e)

# except Exception as e:
#     print("Some other problem happened")
#     print(e)

# print("End")
# try:
#     print("Start")

#     try:
#         print(10 + "5")   # TypeError
#     except TypeError as e:
#         print("Inner problem: type mismatch")
#         print(e)

# except Exception as e:
#     print("Outer problem happened")
#     print(e)

# print("End")
# try:
#     int("abc")try:

# except ValueError:
#     print("Handled")
#     raise
try:
    try:
        int("abc")
    except ValueError:
        print("Inner handled")
        raise
except Exception:
    print("Outer handled")

print("End")
try:
    raise ValueError("X")
except ValueError:
    print("Handled")
# try:
#     pass
# finally:
#     raise Exception("Forced")
try:
    print("Start")
    raise KeyError("missing")
except Exception as e:
    print("Caught")
    raise
print("End")
try:
    try:
        int("abc")
    except ValueError:
        print("Inner except")
        raise
except ValueError:
    print("Outer except")
finally:
    print("Finally block")



