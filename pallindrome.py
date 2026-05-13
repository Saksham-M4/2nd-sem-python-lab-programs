# Program to check palindrome using lambda

string = "madam"

palindrome = lambda s: s == s[::-1]

print("String:", string)

print("Is Palindrome:", palindrome(string))