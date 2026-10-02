# def total(*args):
#     sum = 0
#     for num in args:
#         sum = sum + num
#     return sum
# print(total(10, 20))
# print(total(10, 20, 30))

# def identity(**kwargs):
#     for key, value in kwargs.items():
#         print(key,value)
# identity(name = "manu", age = 18)       
# def test(*args):
#     print(args)

# test(1, 2, 3)
def show(**kwargs):
    for k, v in kwargs:
        print(k, v)
# def calc(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# print(calc(2, 4, 6))
# def info(**kwargs):
#     for key in kwargs:
#         print(key)

# info(name="Manu", age=18)
def demo(a, *args):
    print(a)
    print(args)

demo(10, 20, 30, 40)
def show(**kwargs):
    print(kwargs.get("age", 0))

show(name="Manu")
def test(*args, **kwargs):
    print(len(args), len(kwargs))

test(1, 2, a=10, b=20)
def values(**kwargs):
    for item in kwargs:
        print(item)
def outer():
    def inner():
        return 5
    return inner

x = outer()

def func(a, b, c):
 print(a, b, c)

vals = (1, 2, 3)
func(*vals)


