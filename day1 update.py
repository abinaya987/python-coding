#1.variable Basics
Name="Abinya"
print(Name)

#2.comparison Operators
Num=int(input("Enter The Number"))
if Num>10:
   print("Big")
else:
   print("Small")
   
#3.Even or Odd
Num=int(input("Enter The Number"))
if Num%2==0:
    print("Even")
else:
    print("Odd")
    
#4.if-elif Ladder
Num=int(input("Enter The Number"))
if Num>0:
    print("Positive number")
elif Num==0:
    print("zero")
else:
    print("Negative Number")
        
#5.Nested If - Number Range
Num=int(input("Enter The Number"))
if Num>0:
    print("Positve Number")
    if Num<100:
     print("The Number is Less Then 100")
    else:
     print("The Number is Greater Then 100")
else:
    print("The Number is Not Positive")

#6.Multiple Conditions With Oprators
age=int(input("enter the age"))
height=float(input("enter the height"))
if age>=18 and height>=150:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you can't ride")

#7.Largest of Three Number (if-elif)
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2:
 if num1>num3:
    print("the largest number is num1")
else:
    print("the largest number is num3")
    
if num2>num1:
  if num2>num3:
    print("the largest number is num2 ")
else:
    print("the largest number is num3")
    
#8.Nested if- Grade system
Marks=int(input("enter the Mark"))
if  Marks >=50:
 if Marks >75:
    print("Distinction")
 else:
    print("pass")
else:
    print("fail")
    
#9.Logical Operators
Num=int(input("enter the number"))
if Num%3==0 and Num%5==0:
    print("the number divisible by both 3 and 5")
else:
    print("the number is not divisible by both 3 and 5")
    
#10.Odd and positive
Num=int(input("enter the number"))
if  Num>0 and Num%2!=0:
    print("Positive Odd")
else:
    print("Dosen't match")
    
#11. username & positive check(nested)
Username=input('enter the username')
password=input("enter the password")
if Username=="admin":
    if password=="1234":
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("Unknown username")

#12 compare two variables
a=int(input("enter the A value"))
b=int(input("enter the B value"))
if a>b:
    print("A is Bigger")
elif a==b:
    print("Equal")
else:
    print("B is Bigger")

#13 Multiple elif -month days
Month=input("enter the month name:")
if Month in("january","march","may","july","august","october","december"):
    print("31 days")
elif Month in("april","june","september","november"):
    print("30days")
elif Month == "February":
    print("28 or 29 days (depending on leap year)")
else:
    print("Invalid month name ")

# #14. Nested if- Discount Offer
Amount=int(input("Enter the Amount"))
if Amount>=1000:
    if Amount>=5000:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")
    
#15. Odd/Even with Nested if
Num=int(input("enter the number"))
if Num %2==0:
    if Num %4==0:
        print("Even and divisible by 4")
    else:
       print("even but not divisible by 4")
else:
    print("Odd Number")


    