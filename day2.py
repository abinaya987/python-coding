#List Question
#1.without reverse function
list=["HTML","CSS","PYTHON","JAVA"]
reversed=list[ : :-1]
print(reversed)

#2.using for forloop
nums=[ 2, 4, 6, 8, 10]  
total=0
for i in nums:
    total += i
    print("the sum is:",total)

#3.romove duplicate elements
list=[10,20,30,40,10,60,70,10,80,10,90]
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)

#Tuple Questions
#4.print 2nd and 4th element
Numbers=(10, 20, 30, 40, 50)
second=Numbers[1] 
fourth=Numbers[3]
print(second)
print(fourth)

#5.check the number is tuple
number=(10,20,30,40,50)
num=int(input("enter the number"))
if num in number :
    print("number exists in the tuple")
else:
    print("number does not exists in the tuple")

#Dictionary Ouestions
#6.cost of fruits 
fruits={"Apple":70, "Banana":40, "Orange":50, "Mango":60, "Grapes":80}
print("fruits costing more than 50: ")
for fruit,price in fruits.items():
    if price > 50:
        print(fruit)

#7.Add for key and value in dictionary
fruits={"Apple":70, "Banana":40}
new_fruit=input("Enter the Fruits Name: ")
new_price=int(input("Enter the price : "))
fruits[new_fruit]=new_price
print ("updateD dictionary: ",fruits)

#8.merge two dictionary
dict1={"Orange":60, "Mango":70, "Avocado":100}
dict2={"Potato":30, "Onion":50, 'Cauliflower':40}
Merged_dict=[dict1 | dict2]
print(Merged_dict)
    
#Set Ouestion
#9.find union and intersection
setA={1,2,3,4,5}
setB={3,4,5,6,7}
UnionSet=setA.union (setB)
print("Union of Sets: ", UnionSet)
InterSectionSet=setA.intersection (setB)
print("InterSection of Sets: ",InterSectionSet)

#10.Check the number is set
Number={10,20,30,40,50,60}
set=int(input("Enter the Number"))
if set in Number:
    print("The Number exists in the Set")
else:
    print("The number does not exists in the Set")
 
#String Question
#11.Check the string is palindrome
Str=input("Enterr the String: ")
Str=Str.lower()
reversed_Str=Str[ : :-1]
if Str == reversed_Str:
    print("The String is Palindrome")
else:
    print("The String is Not Palindrome")

#12.number of vowels count in string
text=input("Enter the String:")
text=text.lower()
count=0

for ch in text:
    if ch in "aeiou":
        count += 1
        
print("Number of vowels in the String: ",count)
        
#Loop Questions
#13.Multiplication table using for loop
Number=int(input("Enter the Number"))
for i in range(1, 11):
    Table= Number * i
    print(Number,"x", i, "=", Table )
    
#14.print number 1 to 50 ussing for while loop
i=1
while i<=50:
    print(i)
    i=i+1

#15.type exit the program is end
while True:
    user_input = input("Enter something: ")
    if user_input.lower() == "exit":
        print("Program ended.")
        break

    