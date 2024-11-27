#Factorial of a Number
'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))'''

#Fibonacci Series
'''def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''

#Sum of Natural Numbers
'''def sum_natural(n):
    if n==1:
        return 1
    return n + sum_natural(n-1)
print(sum_natural(5))'''

#Check if a string is a palindrome
'''def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar"))'''

#Power of a number
'''def power(x,y):
    if y==0:
        return 1
    return x*power(x,y-1)
print(power(2,3))'''

#GCD
'''def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
print(gcd(48,18))'''

#Decimal to Binary
'''def decimal_to_binary(n):
    if n==0:
        return ""
    return decimal_to_binary(n//2)+str(n%2)
print(decimal_to_binary(10))'''

#Reverse a string
'''def reverse_string(s):
    if len(s)==0:
        return ""
    return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))'''

#Sum of digits of a number
'''def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)
print(sum_of_digits(456))'''

#Product of Array Elements
def product_of_array(arr,n):
    if n==0:
        return arr[0]
    return arr[n]*product_of_array(arr,n-1)
print(product_of_array([1,5,7,9,3],4))