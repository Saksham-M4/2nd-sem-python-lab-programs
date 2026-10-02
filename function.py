
# def f(x):
#     return x + 2

# print(f(f(3)))
# def f():
#     print("A")
#     return
#     print("B")

# print(f())
# def f():
#     return 5

# g = f
# print(g())
# def f():
#     print(1)
#     return 2
 
# print(f() + f())
# def f(x):
#     return x and 5

# print(f(0), f(3))
# def f():
#     return f

# print(f()())
# def outer():
#     def inner():
#         print("Hello")
#     return inner
# x = outer()
# x()
# def outer():
#     x = 10
#     def inner():
#         return x + 5
#     return inner

# f = outer()
# print(f())
# # def outer(x):
# #     def inner(y):
# #         x = x + y
# #         return x
# #     return inner

# # f = outer(10)
# # print(f(5))
# def f():
#     print(1)
#     return 2
    

# print(f() + f() )
# def f():
#     print("Hi")
#     return f

# print(f()())
# def f():
#     return 5

# def g():
#     return f

# print(g()())
# def f():
#     return f

# def g():
#     return f()

# print(g())
# data = ["10", "20", "", "30"]

# result = "-".join(data).join("AB")
# print(result)
def reverse_string(s):
   result = []
   for ch in s:
        result.append(ch)
   return "".join(result[::-1])
print(reverse_string("hello"))










