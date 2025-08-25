#01.Basic question
def greet(greeting):
    print("Hello,",greeting)
greet ('Welcome to Python')
greet ('Welcome to python')
greet ('Welcome to python')

#02.Function with Parameters
def cal(a,b):
    c=a+b
    print('add : ',c)
cal(5,7)

#03.Default Argument
def power(base, exponent = 2):
   return base ** exponent
print(power(5))

#04 Function with Return value
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(5))
print(is_even(8))
   

#05.Function with List Input

def find_max(lst):
    return max(lst)
print(find_max([10,20,30,40,50]))

#06.Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#07 Fuction with *args
def total_sum(*numbers):
    return sum(numbers)
print(total_sum(10,20,30))

#08.Function with **kwargs
def student_details(**info):
    for key,value in info.items():
        print(key, ":", value)
student_details(name="sam",age="20",course="python")

#09 NestedbFunction
def outer():
    def inner():
        print("call inner function")
    inner()
outer()

#10 Function with string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("python"))


    



     
