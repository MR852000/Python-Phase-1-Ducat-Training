
 
# what is a used of Print funcation in python 
"""Print funcation is a method that check the code in a terminal """
Name="Msood Rahman"
Age = 25
My_place = "New Delhi"
print("Hi my name is",Name,"and my age is",Age,"from ",My_place)
"""Comma method, F-string function, Concatenation+ to wrint print() funcation"""

ph="7303367532"
print(f"my phone nuber is {ph}")

#Coments in python 
#Single Coment 
#Multiple Coment means Docstrean
"""""" and''''''
#Escape Sequeances or Escape Charectar
"""
\' Single quotation Escape Sequance 
\" Double quotation Escape Sequance 
\n next line  Escape Sequance 
\b Backspace  Escape Sequance 
\t Tab Sequence 
"""
print("Hi my name is Masood Rahman\nMy age is 25\nfrom New Delhi....")
print("Hi my name is masood rahman\bMy age is 25\bfrom new Delhi....")
print("Hi my name is \'masood rahman\'. My age is 25 from new Delhi....")
print('Hi my name is "M"\t\t\tasood Rahman')
print('Hi my name is \"Masood Rahman\"')
print("Hi my name is \\nMasood Rahman")

# Variable 
"""
An according to python programming language variable it is a contaner that stored any data type 
in a particula memory indexing like Stack and Heap"""
x=10
y=20
print(x*y)
# Input funcation 
"""
An according to Data Analyst Input funcation is basicaly used in access the 
paritucal data set in  CSV file or Database is called data Input funcation.
"""

num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
num_3=int(input("Enter third number: "))
Total=num_1+num_2+num_3
print(f"Now the total sum is = {Total}")
name=input("Enter your Name:")
age=input("Enter your age:")
gender=input("Enter your Gender:")
print(f"Hi {name}")

# Data Type
"""Data type specifies which type of value to store on a variable has and what mathematical relation 
or logical operation can be perfomed on it without causing any eror is called Data Type. """

"""
(i) Numeric Data Types:	int, float, complex
(ii) Sequence Data Types: Str, list, tuple, range
(iii) Mapping Data Type:	dict
(iv) Set Data Types:	set, frozenset
(v) Boolean Data Type:	bool
(vii) Binary Data Types:	bytes, bytearray, memoryview
(viii) None Data Type:	NoneType
"""
a=[88,44.4,True,"Masood Rahman"]
print(a[1])
print(f"{type(a[1])}\n")
# Itration

print("Now we used a itration by using a for loop in list ellement step by step ")
Rahman_family=["Masood Rahman","Masooma Rahman","Rabeya Rahman"]
# first count the all ellement in a list by using len () 
Total_ellement=len(Rahman_family)
print(f"The total ellement on list = {Total_ellement}")
#Now know that in this list have three ellement have over their
for i in range(0,3):
    print(Rahman_family[i])
    
# Itrate by Position or Index 
print("----------************-------------")

Rahman_family=["Masood Rahman","Masooma Rahman","Rabeya Rahman"]
for i in range (len(Rahman_family)):
    print(Rahman_family[i])
# Itrate by value 
Rahman_family=["Masood Rahman","Masooma Rahman","Rabeya Rahman\n"]
for i in Rahman_family:
    print(i, end=" ")

print("""#write the list your own self and print reverse\n""")
Masood_info = ["Masood Rahman", "8 May 2000", 7303367532]
# Start at index 2, end at 0, step by -1
for i in range(len(Masood_info) - 1, -1, -1):
    print(Masood_info[i])
# Sequence data type str
"""Str"""
"""List :- to store any type of value in a variable like string, boolea, integer, float, double """
# Write your own list and print only even number
Num=[1,2,3,4,5,6,7,8,9,10]
print("This are even number ellement over the list ")
for i in Num:
    if i %2==0:
        print(i)
# Write your own list and print only odd number
Num=[1,2,3,4,5,6,7,8,9,10]
print("This are odd number ellement over the list ")
for i in Num:
    if i %2!=0:
        print(i)
# Write the own list and print the even number index using len() 
Num=[1,2,3,4,5,6,7,8,9,10]
print("This are even number indexing ellement over the list ")
for i in range (0,len(Num)):
    if Num[i] %2==0:
        print(Num[i],end=" ")

#Make own your list and sum all number ellement
Num=[1,2,3,4,5,6,7,8,9,10]
total=0
for i in Num:
    total=total+i
print(f"\nsum all number ellement = {total}")

#Make own your list and sum all number ellement
Num=[1,2,3,4,5,6,7,8,9,10]
print("This are even number indexing sum of ellement over the list ")
for i in range (0,len(Num)):
    total=total+i
print(total)

# Make in your own list. count the number of even number present in that list 
List_1=[100,99,98,97,9678,44,34,33]
count=0
for i in List_1:
    if i % 2==0: # even number logic within condition 
        count=count+1
print(f"The even number of ellement in the list = {count}")

# Make in your own list. count the number of odd  number present in that list
List_1=[100,99,98,97,96,78,44,34,33]
count=0
for i in List_1:
    if i % 2!=0: # odd number logic within condition 
        count=count+1
print(f"The odd number of ellement in the list = {count}")

# Make in your own list. count the number of even number present and sum the all ellement
List_1 = [100, 99, 98, 97, 96, 78, 44, 34, 33]
total = 0
for i in range(0, len(List_1)):
    if List_1[i] % 2 == 0:
        total = total + List_1[i]
print(f"The sum of even number ellement in the list = {total}")
# Make in your own list. count the number of odd number present and sum the all ellement
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count_3 = 0
count_4 = 0
for i in num:
    # Check for 3 independently
    if i % 3 == 0:
        count_3 += 1
    # Check for 4 independently
    if i % 4 == 0:
        count_4 += 1
print(f"Elements divisible by 3 = {count_3}") 
print(f"Elements divisible by 4 = {count_4}") 

# Make the list and check the whic is positive and negative 
Whole_num = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
"""-10-------------0------------10"""
count_negative = 0
count_positive = 0
for i in Whole_num:
    if i <= 0:
        count_negative += 1 
    elif i >= 0:
        count_positive += 1

print(f"Negative Elements = {count_negative}") 
print(f"Positive Elements = {count_positive}")
# Make the list and print the largest number in the present list 
my_list=[100,101,1001,200,300,400,1000]
largest =0
for i in range (0,len(my_list)):
    if my_list[i] > largest:
        largest=my_list[i]
print(f"The Largest number in theis list = {largest}")
"""List :-List is a Mutable sequence data type to store any type of value in a variable like
 string, boolean, integer, float is called List """
# Mutabel means to easily manupilate the present data like append and pop 

# List Method append pop remove
num_1=[1,2,3,4,5,6,7,8,9,10]
print(num_1)
"""append() is to storre a data in list position"""
num_1.append(11)
print(num_1)
"""insert() is store the data by the basis of Memory Indexing  which means 13 is a memory index position and data is '12'"""
num_1.insert(13,12)
print(num_1)
"""Now we used POP """
num_1.pop(-1) # last digit removed from negative indexing 
print(num_1)
num_1.clear()
print(num_1)# all ellement removed by used clear() fucation 

"""Write the program from user that entert the number ellement as form list"""
# Ask the user for the length of the list
length = int(input("How many numbers do you want in your list = "))
# Initialize an empty list
user_list = []
# Use a loop to populate the list
for i in range(length):
    num = int(input(f"Enter element {i + 1}: ")) # i is used for enter the ellement +1 is used for Indexin
    user_list.append(num)
print(f"The final List : {user_list}")

"""write the element and removed even number from the list """
list_=[1,2,3,4,5,6,7,8,9,10]
result=[]
for i in range(0,len(list_)):
    if i % 2!=0:
        result.append(i)
print(result)

"""Make a list which have 1 to 10 ellement over thier and 
sapreate the elementas odd list and even list """
# Member ship operator in list 
my_info = ["Masood Rahman", "DOB 8 May 2000", "Ph no:7303367532"]

print("Masood Rahman" in my_info)
# 2. Checks for "Sonu"
if "Sonu" in my_info:
    print(True)
else:
    print(False)

# 3. User input check
user_info = input("Enter the number which present on the list : ")
if my_info.count(user_info) > 0:
    print(True)
else:
    print(False)
"""""Make your own list and removed dulicate value"""
my_list=[1,2,3,4,5,5.5,3,4,5,"Masood Rahman"]
result=[]
for i in my_list:
    if i not in result: # removed duplicate value 
        result.append(i)
print(result)

"""Make a list that check the element from the user if the number exisist in the list the print 
the position of the element else print -1 """
My_list=[10,20,30,40,50,"Sonu",50.5]
value=input("Enter the Value to Check over the element: ")
if value in My_list:
    index=My_list.index(value)
    print(f"Yes the element are present = {index} index position")
else:
    print(-1)
"""Make a list that from user end  check the element from the user and then 
copy the all element to store in revresd order"""
My_list=[]
for i in range(5):
    value = int(input(f"Enter the all Element [i] = "))
    My_list.append(value)
result=[]
for i in range (len(My_list)-1,-1,-1):
    result.append(My_list[i])
print(f"The final list revesr formate  = {result}")

"""Make a int number list and calculate the average value ot he list """
mylist=[1,2,3,4,5]
average=sum(mylist)/len(mylist)
print(average)
"""Write the progamm that check the value in a list highest occureance  and print element"""
MY_list=[5,8,9,10,6,5,9,8,10,5]
result=[]
for i in MY_list:
    if i not in result:
        result.append(i)
highest_ocurence_value=0
highest_occurence=0
for i in result:
    Count=MY_list.count(i)
    print(f"{i} occure the highest value in {Count} Times ")
    if Count>highest_occurence:
        highest_occurence=Count
        highest_ocurence_value=i
print(f"Highest occurence element is = {highest_ocurence_value}")  

"""make the two list to find a common element and saved in third list as a name of result"""
num_1=[1,2,3,4,5,6,7,8,9,10]
print(f"num_1 list = {num_1}")
num_2=[5,10,15,20,25,30,35,40]
print(f"num_2 list ={num_2}")
result=[]
for i in num_1:
    if i in num_2:
        if num_1 not in result:
            result.append(i)
print(f"The coman ellment is result list = {result}")

"""Make the list and find a second largest value value in the list without using sorting """

my_list = [10, 50, 80, 990, 880, 500, 670, 986, 980, 1020, 5024, 890, 7, 6, 4, 2, 0]
largest = float('-inf')
second_largest = float('-inf')
for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i

print(f"The Secod largest number in the list = {second_largest}")
    
"""Make the kist to make product of sum """
my_list = [10, 50, 80, 990, 880, 500, 670, 986, 980, 1020, 5024, 890, 7, 6, 4, 2] 
P_Sum=1
for i in my_list:
    P_Sum=P_Sum*i
print(f"The sum of product on the list {P_Sum}")   
import math
my_list = [10, 50, 80, 990, 880, 500, 670, 986, 980, 1020, 5024, 890, 7, 6, 4, 2,]
print(f"The final Product using math.prod () ={math.prod(my_list)}")


"""Make a list and check the the prime number over theire or not!"""
my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in my_list:
    factor=0
    for i in range (1, num + 1):
        if num%i==0:
            factor+=1
    if factor==2:
        print(f"Prime number = {num}")
"""Make a list and split into two part"""
Orignal=[100,20,30,500]
first_halfe=Orignal[:len(Orignal)//2]
second_half=Orignal[len(Orignal)//2]
print(f"First halfe List {first_halfe}")
print(f"Second halfe List {second_half}")

# List Itration 
my_list=[]
for i in range(1,21):
    my_list.append(i)
print(my_list)
"""List Comprehension is the method to understand when  
we enter the element on a single line of code at 
list so we used Comprhension and it's faster and acurate """
mylist=[i for i in range(1,21)]
print(mylist)
            
num_list=["Even" if i % 2==0 else "Odd"  for i in range(1,21)]
print(num_list)
"""Make a Comprhension List for even number """
Num_list=[i for i in range (1,31) if i % 2 ==0]
print(f"Even Number List = {Num_list}")
"""Make a Comprhension  List for the odd number"""
Num_list = [i for i in range (1,31) if i % 2 !=0]
print(f"Odd Number List = {Num_list}")

"""Make a List which start and end with from user input element and check the thoes ellement are divde by 2 and 3"""
Start=int(input("write the starting Element = "))
End=int(input("write the ending Element = "))
List=[i for i in range (Start,End+1) if i %2 ==0 and i % 3==0]
print(List)
print("***----------********------------****\n")
# List Slicing
num=[i for i in range (1,21) ]
print(num)
a=num[0:5]
print(f"for positive slicing = {a}")
b=num[-1:-7:-1]
print(f"for Negative slicing = {b}")
c=num[10:15]
print(f"for mid value indexing= {c}")

"""Make a list Comprhension to make positve, mide, negative slicing index """
Usr_start=int(input("Enter the element start = "))
Usr_end=int(input("Enter the element to end = "))
Num=[i for i in range (Usr_start,Usr_end+1)]
a=Num[0:5]
print(f"for positive slicing at user end = {a}")
b=Num[-1:-7:-1]
print(f"for Negative slicingat at user end = {b}")
c=Num[10:15]
print(f"for mid value indexing at at user end = {c}")

count = int(input("Enter how many elements you want in the list: "))
user_list = []
result = []
for i in range(count):
    val = int(input(f"Enter element {i+1}: "))
    user_list.append(val)
for num in user_list:
    if num % 2 != 0:
        result.append(num)

"""Creating a list using prompt and make a list then we take a one old ellement pick 
after that update them from the user end """
# 1. User input
total_elements = int(input("Enter how many numbers you want = "))
result = []
for i in range(total_elements):
    num = int(input(f"Enter number {i+1} = "))
    result.append(num)
# 2. print the output 
print(f"Your final list: {result}")
index_to_update = int(input(f"Enter the index you want to update (0 to {len(result)-1}) = "))
if 0 <= index_to_update < len(result):
    new_value = int(input("Enter the new value = "))
    # 3. Update the element from the user end
    result[index_to_update] = new_value
    print(f"Updated list: {result}")
else:
    print("Invalid index! Please pick a number within the list range.")
"""Enter the user input how much element you want and divide by user 
input check element are divde or not divide"""
# Code
total_elements = int(input("Enter how many numbers you want = "))
result = []
for i in range(total_elements):
    num = int(input(f"Enter number {i+1} = "))
    result.append(num)
divisor = int(input("Enter the number to divide by: "))
divisible_list = []
not_divisible_list = []
for num in result:
    if num % divisor == 0:
        divisible_list.append(num)
    else:
        not_divisible_list.append(num)
# Print the output
print(f"\nOriginal List: {result}")
print(f"Numbers divisible by {divisor}: {divisible_list}")
print(f"Numbers not divisible by {divisor}: {not_divisible_list}")

a=[10,9,8,7,6,5,4,3,2,1, 0.5]
print(a)
a.sort()
print(f"We uppdate value using sort () and we have know {a}")
#update the data
# Index
position=a.index(0.5)
print(f"'0.5' element memeory address = {position} position")
# Now we add the value in last position of a list 
a.append("Masood Rahman")
print(f"Using the append () we add the new element = {a}")
a.extend(["Masooma Rahman","Rabeya Rahman"])
print(f"Now we used extend([]) to add element in list:- \n{a}")
# now check the repetade ellement in list 
repeted=a.count("Masood Rahman")
print(f"the number of 'Masood Rahman' element at count is {repeted} time")
"""Make a list which have 1 to 10 ellement over thier and 
sapreate the elementas odd list and even list """
List=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(0,len(List)):
    if List[i] % 2==0:
        even.append(List[i])
    else:
        odd.append(List[i])
print(f"The Even element in this list = {even}")
print(f"The Odd element in this list = {odd}")

"""Make two list with random number and merge both in different list"""
List_1=[1,2,3,4,5]
List_2=[6,7,8,9,10]
Result=[]
for num in range(0,len(List_1)):
    Result.append(num)
for num in range (0,len(List_2)):
    Result.append(num)
print(f"The merge List_1 and List_2 = {Result}")


Result=List_1+List_2
print(f"without zero = {Result}")

# Tuple 
"""Tuple :- Tuple is is sequence and immutable data type means when you store a data 
we can't manupilate the data in python"""
my_tuple=(1,2,3,4,5,1,2,5)
print(type(my_tuple))
print(f"my_tuple data ={my_tuple}")
#Now we check the element using count in tuple 
Count=my_tuple.count(5)
print(Count)
# Indexing
print(f"In my_tuple Indexing in zero indexing = {my_tuple[0]} element number located ")
#chek the element index 
Index=my_tuple.index(4)
print(f"In tuple '4' element number of indexing = {Index}")
# example of immutable in tuple 
#my_tuple[0]=100
#print(f"As you can see the data we not manuplilate show give bellow ={my_tuple}")

"""Making a list and print the element using for loop """
My_tup=(1,2,3,4,5)
for i in My_tup:
    print(i)
    
# User inputs for start and end
usr_starte_tuple = int(input("Enter the element start = "))
usr_end_tuple = int(input("Enter the element end = "))

# Using a generator expression inside the tuple() constructor
# This is the standard way to "comprehend" a tuple
My_Tup = tuple(i for i in range(usr_starte_tuple, usr_end_tuple + 1))

# Printing the final tuple
print(f"Your Start and End elements stored in My_Tuple = {My_Tup}")

"""Make a Tuple by user start and end of ellement 
using comprehension and print and check the ellement which was divisble 2 and 3"""
usr_starte_tuple = int(input("Enter the element start = "))
usr_end_tuple = int(input("Enter the element end = "))
My_Tup = tuple(i for i in range(usr_starte_tuple, usr_end_tuple + 1) if i % 2 ==0 and i % 3 ==0)
print(f"In the user end  element are divisble by 2 and 3 is = {My_Tup}")

"""Now we make add the element value in tuple as we know that tuple is immutable?"""
Tup=(1,2,3,4,5)
print(f"first we have only 1 to 5 element only {Tup}")
# Conversion in tuple to list
My_List=list(Tup)
My_List.append(6)
Tup=tuple(My_List)
print(f"Now we have a 6 also using conversion {Tup}")

# String data type 
"""String is a  Sequence Immutable data type and it will ittrable also is called String """
# Example 
Introduction="Hi my name is Masood Rahman and i am from New Delhi"
print(Introduction)
print(type(Introduction))
# Now we try to update 
#Introduction[0]="M"
print(f"As you can see that we have a show a error {Introduction} that mean's this is Immutable")
# Now we check the Indexing 
print(f" Check the in zero Indexing value = {Introduction[0]}\n")
# Now we used Itration
for j in Introduction:
    print(f"{j}\n")
# Now we check Itrable 
for i in range(0,len(Introduction)):
    print(i, end=" ")
# Negative Indexing using Itrable 
for i in range(len(Introduction)-1,-1,-1):
    print(f"\n Negative Indexing = {i}")

# Different operation of a string 
# add the two string 
First_name="Masood "
print(First_name)
Laste_name="Rahman"
print(Laste_name)
full_name=First_name + Laste_name
print(f"we used concatenation = {full_name}")
# Multiply the operation in string
print(f"\n{First_name*2}")

"""ASCII Code:- we have comparision operation predine funcation ord()"""
name = "Masood"
for char in name:
    print(f"{char}: {ord(char)}")
print("-----*****-----")
Name = "masood"
for Char in Name:
    print(f"{Char}: {ord(Char)}")
# Comparison operation using ASCII
if name < Name:
    # Lowercase letters have higher ASCII values than Uppercase
    print(f"\n'{name}' is smaller because {name[0]} ({ord(name[0])}) < {Name[0]} = ({ord(Name[0])})")
elif name > Name:
    print(f"\n'{name}' is larger because {name[0]} ({ord(name[0])}) > {Name[0]} = ({ord(Name[0])})")
else:
    print(f"\n{name} = {Name} both are equal")

"""Make user end email id ASCII value check"""
email=input("Enter your valid email id = ").strip()
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(email)
for S_chr in email:
    print(f"{S_chr}: {ord(S_chr)}")

"""Comparision betwen two user email id for ASCII value """
import re
Usr_1 = input("Enter 1st email id: ").strip()
Usr_2 = input("Enter 2nd email id: ").strip()
# Comparison logic
if Usr_1 < Usr_2:
    print(f"\n'{Usr_1}' is < '{Usr_2}' based on ASCII order.")
elif Usr_1 > Usr_2:
    print(f"\n'{Usr_1}' is > '{Usr_2}' based on ASCII order.")
else:
    print(f"\nBoth email IDs are identical are equal.")
# To see specific ASCII values of the first characters:
print(f"ASCII of '{Usr_1[0]}': {ord(Usr_1[0])}")
print(f"ASCII of '{Usr_2[0]}': {ord(Usr_2[0])}")

# Slicing in String
introduction="Hi my name is Masood Rahman"
# right to left slicing idex
Slicing_Index=introduction[0:20]
print(Slicing_Index)
slicing_index=introduction[::-1]
print(f"{slicing_index}\n")
"""make user end string and check the palindrom or not """
my_string=input("Enter the word : ")
if my_string==my_string[::-1]:
    print("Yes it's palindrome")
else:
    print("No it's not palindrome")
# Sring Method 
name = "masood rahman"
print(name)
capital=name.capitalize()
print(capital)
Title=name.title()
print(Title)
Upper=name.upper()
print(Upper)
Lower=name.lower()
print(Lower)
Swapcase=name.swapcase()
print(Swapcase)
# String Boolean Method
a=name.isupper()
print(f"All element are Capital later.    __{a}__")
b=name.islower() 
print(f"All element are small later.      __{b}__")
c=name.istitle()
print(f"All element are Capital.          __{c}__")
d=name.isalpha()
print(f"In this string have present space. __{d}__")
e=name.isalnum()
print(f"This string have only alphabet or number.___{e}__")
f=name.isspace()
print(f"This string have present space __{f}__")

intro="25"
print(intro,type(intro))
if intro.isdigit():
    intro=int(intro)
    print(f"They convert into string to integer :{intro,type(intro)}")
else:
    ("Not convert into integer ")

"""Make a string data type all elemenyt are small then convert into Capital """
Name="masood rahman"
up=Name.upper()
print(up)

"""Make a string and count the how many alphabet using ASCII """
Intro="Masood Rahman"
count=0
for chr in Intro:
    ASCII=ord(chr)
        # for small chr              # for Cpital 
    if (ASCII>=65 and ASCII<=90) or (ASCII>=97 and ASCII<=122):
        count=count+1
print(count)

"""Ask a string from user end. And count the 
number of alphabet over there string using for loop itration"""
Usr=str(input("Write the Statement! "))
for char in Usr:
    print(char)
count = 0
for char in Usr:
    if char.isalpha():
       count += 1
print("-----")
print(f"Total nunmber of alphabet count is = {count}")

"""Write the program from user end string data and check the number of UPPER() and LOWER()
"""
Usr=str(input("Enter the Statement! "))
Upp=0
Low=0
for chr in Usr:
    print(chr)
    if chr.isupper():
        Upp+=1
print("---------")
print(f"Total Upper case = {Upp}")
for Chr in Usr:
    print(Chr)
    if Chr.islower():
        Low+=1
print("--------")
print(f"Total Lower case = {Low}\n")

"""Ask from the user end as a string data and checkthe 
the number of upper and lower case using ASCII condition"""
Usr=str(input("Enter the Statement! "))
Upp_count=0
Low_count=0
for chr in Usr:
    ASCII=ord(chr)
    if ASCII >= 65 and ASCII<=90:
        Upp_count+=1
    elif ASCII >= 97 and ASCII<=122:
        Low_count+=1
print(f"ASCII Capital later = {Upp_count}")
print(f"ASCII Small later = {Low_count}\n")

"""Ask the user end string data type and convert into Upper case and Lower case"""
Usr=str(input("write the small str statement! "))
upp=""
for ch in Usr:
    upp+=ch.upper() 
print(f"usr statement '{Usr}' convert into --> {upp} captial later\n")

"""Ask the user end string data type and convert into Upper case and Lower case"""
Usr=str(input("write the capital str statement! "))
Low=""
for ch in Usr:
    Low+=ch.lower() 
print(f"usr statement '{Usr}' convert into --> {Low} captial later")

"""Ask the user end string data type convert upper case to lower case 
and lower case to upper case condition """
Usr = input("Write the str statement! ")
swapped = ""
for ch in Usr:
    if ch.isupper():
        swapped += ch.lower()  # Convert uppercase to lowercase
    elif ch.islower():
        swapped += ch.upper()  # Convert lowercase to uppercase
    else:
        swapped += ch          # Keep symbols/numbers as they are

print(f"Swapped string: {swapped}")

"""Write user end input and count a space"""
usr=str(input("write introduction : "))
space_count=0
for ch in usr:
    if ch == " ":
       space_count+=1   
print(f"Total number of space = {space_count}")

# Topic Split and Join
"""In a string sequence data type split function used in to removed space"""
Intro="Hi my name is Masood Rahman and i am 25 year old"
print(Intro,type(Intro))
Split=Intro.split()
print(f"As you can see that the String data list using split()\n{Split}")
#"""problem no.1"""
Intro="Hi-my-name-is-Masood-Rahman-and-i-am-25-year-old"
Split_intro=Intro.split("-")
print(Split_intro)
print(f"The total length = {len(Intro)}")
""" In a string data type join funcation is used to convert into list to string"""
#Eexample
List=['Hi', 'my', 'name', 'is', 'Masood', 'Rahman', 'and', 'i', 'am', "25", 'year', 'old']
print(List,type(List))
Join_intro=" ".join(List)
print(f" As you can see that list convert into string = {Join_intro} and data type is {type(Join_intro)}")
# Drawback join () used only all element are str
List=['Hi', 'my', 'name', 'is', 'Masood', 'Rahman', 'and', 'i', 'am', 25, 'year', 'old']
Join_intro=" ".join(str (i) for i in List)
print(Join_intro,type(Join_intro))

"""Make a string to print in apposite direction
"""
Intro="Hi my name is Masood Rahman"
word=Intro.split()
word=word[::-1]
print(word)

"""Make a string in user end and print apposite direction"""
User=str(input("Tell me about your self : "))
Con_list=User.split()
Con_list=Con_list[::-1]
print(Con_list)

"""Make a user end string the first later of a word it should be caplital"""
User=str(input("Write anything in small later.. : "))
Cap=User.title()
print(Cap)

# String data type :- method->Count(), Replace(), Find(),Strip(), Endswith(),
python="python is a good programming language for the upcoming future"
Count=python.count("a")
print(f"The number of count of a--> is {Count}")
Check_word=python.startswith("python")
print(Check_word)
address=python.index("l")
print(address)
Replace=python.replace("p", "P")
print(Replace)
Intro="@@@@@@@Hi my name is Masood Rahman and i am from delhi@@@@@@@@" 
print(Intro)
# this strip () used on whatsup, Ai chatbot,
removed = Intro.strip("@")
print(removed)
print("""--------------Sequence data type is complete-----------------------""")

# Maping Data Type:- Dictionary 
"""An according to python programing language Dictionary mutable maping data type 
is verry coman and verry verry used full in different Domain aspect 
to build a logic. 
like:-Ai,Ml,Data Analyst, Data Science, Django Developer, Cyber security
and etc. 
"""
BMW={'Car_model':"BMW M5",
     'Owner_name': "Masood Rahman",
     'price':"1.5 cr",
     'Insurance_Id': "DL12789BMW",
    }
print(BMW,type(BMW))
print("---------*********------------\n")
# Get 
My_dic={'Name':"Masood Rahman",
        'Age':25,
        'Gender':"Male",
        'Phone no':7303367532}
print(My_dic)
print(f"Key-> value{My_dic["Name"]}\n")
print(f"{My_dic.get("DOB")}\n")


"""Make user end side Key is existing over the dic if yes then print the value 
else value not found."""

My_info = {
    'Name': "Masood Rahman",
    'Gender': "Male",
    'Age': 25,
    'Phone no': 7303367532
}
# Condition to check the value 
K_valu = input("Enter the Key: ")
result = My_info.get(K_valu)
if result is not None:
    print(f"{result}\n")
else:
    print(f"Key and value does not exist for: {K_valu}\n") 


My_info = {
    'Name': "Masood Rahman",
    'Gender': "Male",
    'Age': 25,
    'Phone no': 7303367532
}
print(f"Curent Dictionary {My_info}\n")
# Add and Update () funcation
My_info.update({'Age':26,'Place':"New Delhi, India"}) 
print(f"Update Dictionary {My_info}\n")

# pop () funcation
My_info={'Name':"Masood Rahman",
         'Gender':"Male",
         'DOB':"8 May 2000",
         'Phone no':7303367532,
         'Place':"New Delhi India"}
print(My_info)
My_info.pop("Phone no")
print(My_info)

# Iterating Key Value Dictionary 
my_info={'Name':"Masood Rahman",
         'Gender':"Male",
         'DOB':"8 May 2000",
         'Phone no':7303367532,
         'Place':"New Delhi India"}
#Keys () funcation
print(f"{my_info.keys()}\n")
"""Now we used Itration only for the key of dictionary """
for Key in my_info.keys():
    print(Key)
#value () funcation 
print(f"{my_info.values()}\n")
for Value in my_info.values():
    print(Value)
"""Using Itrate to print dictionary keys and values using items() funcation"""
print("-------*********--------\nNow we apply itration using items() to print key ans value both")
for key, value in my_info.items():
    print(f"{key} => {value}")
    
"""Make a two different list and convert into a dictionary as a key and value """
#1st List
Student_name=["Masood Rahman","Sonali Ratori", "Hritik Kumar", "Sumit Dang"]
#2nd List 
Student_Class=["Science->Non Med","Comerces","Science-> Medical","Science->Non Med"]
disctionary={}
for i in range (0,len(Student_name)):
    disctionary[Student_name[i]]=Student_Class[i]
for key, value in disctionary.items():
    print(f"{key} => {value}")    
print("\n--------******-------")
"""Ask from the user name class roll no all subject name and marks adding to a dictionary"""
Usr_name = input("Enter your Name: ")
Usr_class = input("Enter your class: ")
Usr_roll_no = str(int(input("Enter the roll no: ")))
Sub_name = {}
Subject_count = int(input("Enter how many subjects: "))
for _ in range(0, Subject_count):
    name = input("Enter subject name: ")
    marks = int(input(f"Enter marks for {name}: "))
    # Add the name as a key and marks as the value to the dictionary
    Sub_name[name] = marks
student_record = {
    "Name": Usr_name,
    "Class": Usr_class,
    "Roll No": Usr_roll_no,
    "Subjects": Sub_name
}
print("\nFinal Student Record:")
for key, value in student_record.items():
    print(f"{key} => {value}")
    
"""Ask from the user name class roll no all subject name and marks adding to a dictionary 
total marks, percentage and Divsion also """
Usr_name = input("Enter your Name: ")
Usr_class = input("Enter your class: ")
Usr_roll_no = str(int(input("Enter the roll no: ")))
Sub_name = {}
Subject_count = int(input("Enter how many subjects: "))
for _ in range(0, Subject_count):
    name = input("Enter subject name: ")
    marks = int(input(f"Enter marks for {name}: "))
    # Add the name as a key and marks as the value to the dictionary
    Sub_name[name] = marks
student_record = {
    "Name": Usr_name,
    "Class": Usr_class,
    "Roll No": Usr_roll_no,
    "Subjects": Sub_name
}
print("\nFinal Student Record:")
for key, value in student_record.items():
    print(f"{key} => {value}")
total = 0
for marks_value in Sub_name.values():
    total += marks_value
print(f"Total Marks: {total}")
max_marks = Subject_count * 100
percent = (total / max_marks) * 100
print(f"Percentage: {percent}%")
if percent <= 95:
    print(f"Congratulation your {percent}% is count on first division")
elif percent>=85:
    print(f"Congratulation your {percent}% is count on Seconnd division")
elif percent ==70:
    print(f"Congratulation your {percent}% is count on third division")
elif percent ==50:
    print(f"{percent} Pass")
else:
    print(f"You are {percent}% fail ")
    
"""Ask a string data type from the uer end. to Display the dictionary where each key is a
 a charectar and value is the frequance of that character that comes in that string 
 """
Usr_str = input("write your statement: ")
freq = {} # 1. Name must match 'freq' used in the loop

for Chr in Usr_str:
     if Chr in freq:
         freq[Chr] += 1
     else:
         freq[Chr] = 1 
print(freq)
for  key, value in freq.items():
     print(f"\n{key} => {value}")
"""given distionary to dictionary"""

Student_record = {
    'Masood Rahman': {"Maths": 85, "Physics": 90, "Chemistry": 78, "Computer Science": 92, "English": 88},
    'Hritik Kumar': {"Bio": 98, "Physics": 97, "Chemistry": 99, "Physical Education": 96, "English": 94},
    'Jai Bhardwaj': {"Maths": 92, "Physics": 88, "Chemistry": 95, "Computer Science": 90, "English": 85},
    'Pravesh Chauhan': {"Maths": 88, "Physics": 75, "Chemistry": 82, "Computer Science": 80, "English": 78}
}
for student, marks in Student_record.items():
    print(f"\n{student} : {marks}") 
    total = sum(marks.values()) 
    percent=total/500*100
    #:.2f used to understand decimal upto two only 
    print(f"{student} Total Mark's: {total} and Percentage: {percent:.2f}%")    

"""Now we check the Student if exsist in dictionary then print the value else student doen't exsist in user end"""
Student_record = {
     'Masood Rahman': {"Maths": 85, "Physics": 90, "Chemistry": 78, "Computer Science": 92, "English": 88},
     'Hritik Kumar': {"Bio": 98, "Physics": 97, "Chemistry": 99, "Physical Education": 96, "English": 94},
     'Jai Bhardwaj': {"Maths": 92, "Physics": 88, "Chemistry": 95, "Computer Science": 90, "English": 85},
     'Pravesh Chauhan': {"Maths": 88, "Physics": 75, "Chemistry": 82, "Computer Science": 80, "English": 78}
 }
user_query = input("Enter the student name: ")

if user_query in Student_record:
    marks = Student_record[user_query]
    total = sum(marks.values())
    percent = total / 500 * 100
    print(f"yes {user_query} Total Mark's {total} and Percentage: {percent:.2f}%")
else:
    print("SORRY student does not exist")
 
"""print the Highst marks and lowest marks"""
Student_record = {
     'Masood Rahman': {"Maths": 85, "Physics": 90, "Chemistry": 78, "Computer Science": 92, "English": 88},
     'Hritik Kumar': {"Bio": 98, "Physics": 97, "Chemistry": 99, "Physical Education": 96, "English": 94},
     'Jai Bhardwaj': {"Maths": 92, "Physics": 88, "Chemistry": 95, "Computer Science": 90, "English": 85},
     'Pravesh Chauhan': {"Maths": 88, "Physics": 75, "Chemistry": 82, "Computer Science": 80, "English": 78}
}

# Initialize variables
highest_marks = 0
lowest_marks = float('inf') # Start with infinity so any score is lower
highest_student = ""
lowest_student = ""

for name, subjects in Student_record.items():
    total = sum(subjects.values()) # Sum the numeric values
    if total > highest_marks:
        highest_marks = total
        highest_student = name
    if total < lowest_marks:
        lowest_marks = total
        lowest_student = name
print(f"Highest Marks: {highest_student} ({highest_marks})")
print(f"Lowest Marks: {lowest_student} ({lowest_marks})")

"""print dic_1 and dic_2 add both in different dic """
dic_1={'a':100,'b':200,'c':300,}
dic_2={'a':200,'b':100,'d':400}
dic_3={}
for Key, Value in dic_1.items():
    dic_3[Key]=Value
for Key, Value in dic_2.items():
    if Key in dic_3:
        dic_3[Key]=dic_3[Key]+Value
    else:
        dic_3[Key]=Value
print(dic_3)
    
"""make a student info"""
Rahaman_family_info={
    #key 1
    "Masood Rahman":{
        "Gender":"Male",
        "Age": 25,
        "Phone no": 7303367532,
        "DOB": "8 May 2000",
            },
    #Key 2
    "Masooma Rahman":{
        "Gender":"Female",
        "Age": 30,
        "Phone no": 9868860369,
        "DOB":"11 May 2000"
        },
    #Key 3
    "Rabeya Rahman":{
        "Gender":"Female",
        "Age":50,
        "Phone no": 9643570575,
        "DOB": "11 April 1973"}
    }
print(Rahaman_family_info["Masood Rahman"])
print(type(Rahaman_family_info["Masood Rahman"]))
print(Rahaman_family_info["Masood Rahman"]["Age"])
print(type(Rahaman_family_info["Masood Rahman"]["Age"]))

Student_info={
    "Masood Rahman":{
        "Physics":89,
        "Chemistry":94,
        "Maths":98,
        "Computer Science":98,
        "English":82
        },
    "Hritik Kumar":{
        "Physics":98,
        "Chemistry":94,
        "Biology":98,
        "Physical Education":98,
        "English":82
        },
    "Pravesh Chuhan":{
        "Physics":98,
        "Chemistry":94,
        "Maths":98,
        "Computer Science":98,
        "English":92
        }
    }
for student_name,student_marks in Student_info.items(): # i will used .values() and sum() funcation
    total=sum(student_marks.values())
    percent=total/500 *100
    print(f"{student_name} => Total Mark's: {total} and pecentage is {percent}%") 
    
Student_info = {
    "Masood Rahman": {
        "Class": "12th Science",
        "Roll no": 12,
        "DOB": "8 May 2000",
        "Marks": {"Maths": 98, "Physics": 96, "Chemistry": 89, "Computer Science": 98, "English": 86}
    },
    "Pravesh Chauhan": {
        "Class": "12th Science",
        "Roll no": 15,
        "DOB": "15 June 2000",
        "Marks": {"Maths": 92, "Physics": 88, "Chemistry": 94, "Computer Science": 95, "English": 90}
    },
    "Hritik Kumar": {
        "Class": "12th Science",
        "Roll no": 16, # Updated to be unique
        "DOB": "15 June 2000",
        "Marks": {"Biology": 92, "Physics": 88, "Chemistry": 94, "Physical Education": 95, "English": 90}
    }
}
for name, details in Student_info.items():
    total = sum(details["Marks"].values())
    percent=total/500 *100
    print(f"Name: {name}")
    print(f"Details: {details}")
    print(f"Total Marks: {total}")
    print(f"Percentage is {percent}%\n")

"""In python Programming language Set's are Mutable Unorder or order sequence data they totaly depend upon code of
structure data type they does not index and position but it is ittrable.
"""
# example 
my_set={4,5,1,3,4,4,4,5,7,"Sonu",66.77,66.77}
print(f"{my_set}\n-------******---------\nNow we used itrate the set ellement using for loop")
"""Itration"""
for ellement in my_set:
    print(ellement)
"""Now we used UNION set math's Logic"""
# Example 
my_set1={9,8,1,7,7,7,8,1,9,10,9}
my_set2={4,5,1,3,4,4,4,5,7}
print(f"SET_1 = {my_set1}")
print(f"SET_2 = {my_set2}")
print(f"UNION SET = {my_set1.union(my_set2)}")
print(f"INTERSECTION SET = {my_set1.intersection(my_set2)}")

"""Make a Two list and check the same ellement"""
List1=[1,2,3,4,5,6,6,8,9]
List2=[6,7,8,4,5,2,2,1,9]
conversion_1=set(List1)
conversion_2=set(List2)
List_3=list(conversion_1.intersection(conversion_2))
print(f"\nThey are common element in List1 and List2 \nList3 = {List_3}")

"""Make a empty set """
my_set={}
print(f"By default they show = {type(my_set)} dictionary data type")
my_set=set()
print(f"They show my_set = {type(my_set)} set data type")

"""add the element of set data """
Set={1,2,3,4,5}
print(f"\n{Set}")
Set.add(6)
print(f"Add the 6 in Set data type = {Set}")
Set.remove(6)
print(Set)

"""Make a set and check user end the element over theire or not"""
My_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Masood Rahman"}

user_input = input("\nEnter the element to check: ")
if user_input.isdigit():
    user_input = int(user_input)
if user_input in My_set:
    print(f"Yes, {user_input} belongs to the {My_set}.")
else:
    print(f"No, {user_input} does not belong to this set  {My_set}.")
"""Make a two List and  check the common element"""
my_List1=[9,8,1,7,7,7,8,1,9,10,9]
my_List2=[4,5,1,3,4,4,4,5,7]
print(set(my_List1) & set(my_List2))
"""make three list and check comon element in list"""
List1=[1,2,3,4,5,6,7,8,9,10]
List2=[2,4,6,8,10]
List3=[0,2,4,6,8,10]
print(f"\nComon element in  List1, List2, List3 ={set(List1)&set(List2)&set(List3)}\n")

"""Make three set and check union element """

Set_2={1,3,5,7,9}
Set_1={2,4,6,8,10}
Set_3={1,2,3,4,5,6,7,8,9,10}
print(f"{Set_1} {Set_2} {Set_3}\n")
Union_result=Set_1|Set_2|Set_3
print(f"Union_result set's = {Union_result}")

"""Write the code to removed all the element in given set"""
Set={1,2,3,4,5,6,7,8,9,10}
Set.clear()
print(f"empty set = {Set}")

"""Wrtie the code to find length in set """
Set={1,2,3,4,5,6,7,8,9,10}
print(f"\n The lenght = {len(Set)}\n")

"""Wrtie the code to find length in set using itration """
Set={1,2,3,4,5,6,7,8,9,10}
count=0
for i in Set:
    count+=1
    print(f"{count}")

"""Make a two set to check element are common over their then print some thing is common"""
Set_1={1,3,5,7,9}
Set_2={2,4,6,8,10}
result=Set_1.intersection(Set_2)
if len(result)==0:
    print(f"{Set_1} and {Set_2} nothing common")
else:
    print(f"{Set_1}and {Set_2} both are someting common")

"""Make user end two different set and check element are common over their then print some thing is common"""
set1 = set(input("Enter elements for first set (separated by space): ").split())
set2 = set(input("Enter elements for second set (separated by space): ").split())
Common = set1.intersection(set2)
if Common:
    # Add the 'f' before the quotes
    print(f"Something is common: {Common}")
else:
    print("Nothing is common.")


# Conditional Statement 
"""An According to Data Analyst Conditional Statement to check the data are exsit 
on value in particular file or database example employe id,age, area region, blood group, salary 
"""
# now we make a Voting Eligibility
name=input("Enter your Name: ")
print(f"Hi {name} let's check your eligibility for voting")
age=int(input("Enter your age: "))
if age>=18:
    print(f"yes {name} you are eligibil for the upcoming vote")
else:
    print(f"No {name} you are not eligibil for the upcoming vote")

Num_1=int(input("Enter the first number"))
Num_2=int(input("Enter the second number"))

if Num_1>= Num_2:
    print("first is larger..")
else:
    print("second is larger..")

Num=int(input("Enter the the = "))
if Num%2==0:
    print("the numner is even")
else:
    print("the number is odd")
    
name=input("Enter your Name: ")
print(f"chek your Result{name}")
Physics=int(input("Enter the the physic number: "))
Chemistry=int(input("Enter the chemistry number:"))
if Physics>=33 and Chemistry>33:
    print("Yes you are Pass {name}....")
else:
    print("Sorry you are fail {name}...\n keep try to next time")

num=float(input("Enter the Number:"))
if num>=0:
    print(f"yes the number {num} is positive..")
else:
    print(f"yes the number is {num} is negative..")

char=input("Enter the charectar: ")
if char=="a"or char=="e"or char=="i"or char=="o"or char=="u":
    print(f"'{char}'a it's a vovel")
else:
    print(f"'{char}' it's a constant")

num_1=int(input("Enter the first number ="))
num_2=int(input("Enter the second number ="))
if num_1%num_2==0:
    print(f"yes it's divide by {num_1} by {num_2}")
else:
    print(f"No it's not divide by {num_1} by {num_2}")
"""Student wil eligibil in 75%"""
Name = input("Enter your Name: ")
Total_of_lecture = int(input("Enter the total lecture = "))
Number_Lecture_attendance = int(input("Enter the no of lecture attend = "))
Student_per = (Number_Lecture_attendance / Total_of_lecture) * 100
print(f"Total percent of attendance is = {round(Student_per, 2)}%")
if Student_per >= 75:
    print(f"Yes {Name}, you are eligible to sit for the end semester exam.")
else:
    print(f"No {Name}, you are not eligible to sit for the exam. Your attendance is only {round(Student_per, 2)}%.")   

# elif 
"""multiple coments handel """
num_1=int(input("Enter first number = "))
num_2=int(input("Enter second number = "))
if num_1>num_2:
    print(f"The first number is greater {num_1}")
elif num_1>num_2:
    print(f"The second number will be greter {num_2}")
else:
    print(f"Both the number are equal {num_1} and {num_2}")
       
"""Write the code to percentage of five subject and make grade at
100 - 90 is A Grade
90 - 80 is B Grade 
80 - 70 is C Grade 
70 - 60 is D Grade 
60 - 50 is E Grade 
"""
name=input("Enter the Student Name: ")
english=int(input("Enter the marks = "))
physical=int(input("Enter the marks = "))
physic=int(input("Enter the marks = "))
chemistry=int(input("Enter the marks = "))
maths=int(input("Enter the marks = "))
Total_marks=english+physical+physic+chemistry+maths
percentage=(Total_marks/500) * 100
print(f"{name} your percentage is {percentage}")
if percentage>90 and percentage>100:
    print(f"Congratulation {name} your Grade is A")
elif percentage>80 and percentage>90:
    print(f"Congratulation {name} your Grade is B")
elif percentage>70 and percentage>80:
    print(f"Congratulation {name} your Grade is C")
elif percentage>60 and percentage>70:
    print(f"Congratulation {name} your Grade is D")
elif percentage>50 and percentage>60:
    print(f"Congratulation {name} your Grade is E")
elif percentage>50:
    print("sory {name} you are Fail butter luck next time ")
    
"""Write the program to check if the number is Odd, Even or positive"""
num=int(input("Enter the number = "))
if num ==0:
    print(f"This number {num} is equla to zero")
elif num %2==1:
    print(f"This number {num} is odd")
else:
    print(f"This number {num} is even")
    
"""write the program user input number is divide by 2 qnd 3 but not 8"""
num=int(input("Enter the number = "))
if num%2==0 and num%3==0 and num%8!=0:
    print(f"yes this number divide by 2 and 3 '{num}' but not '8'")
else:
    print(f"No this number will not divide by 8 in {num} and 2 or 3 also")
"""Write the program that user input  number at last digit number print"""
num=int(input("Enter the number = "))
last_digit_no=num%10
print(f"according to user input {num} and the last digti number is {last_digit_no}")
"""write the program that user input number the last digit number and 
check a condition divide 5 are not"""
num=int(input("Enter the number = "))
last_num=num%10
if last_num==5:
    print(f"Yes the user input {num} at last digit number {last_num} are divide by 5")
else:
    print(f"NO the user input {num} at last digit number {last_num} are not divide by 5")
    
"""Write the program to calculate bill. Ask the final amount from the user you have got 
discount and print the final bill after discount.
50000$ above - 30% discount
40000$ - 35000$ -> 20% discount
35000$ - 20000$ -> 10% discount
20000$ - 10000$ -> 5%  discount"""
user_name=input("Enter your Name: ")
user_bill=float(input("Enter the bill amount = "))
if user_bill>=50000:
    discount=30
elif user_bill>=40000 and user_bill>=35000:
    discount=20
elif user_bill>=35000 and user_bill>=20000:
    discount=10
elif user_bill>=20000 and user_bill>=10000:
    discount=5
else:
    discount=0
print(f"{user_name} you got {discount}% discount")
finall_bill=user_bill-(user_bill*discount/100)
print(f"{user_name} your finall bill amount is {finall_bill} $")

"""Ask the user input number 
* if the numer divisble by 5 then print fizz
* if the number divisble by 3 then print Buzz
8 if the number divisible both 3 and 5 so the Fizz and Buzz
* if the number not divisible form 3 and 5 then print user input number only"""
number=int(input("Enter the number = "))
if number%3==0 and number%5==0:
    print(f"The user input number {number} are divisbel by 3 and 5 so this is Fizz and Buzz both")
elif number%3==0:
    print(f"The user input number {number} is only Fizz")
elif number%5==0:
    print(f"The user input number {number} is only Buzz")
else:
    print(f"The  user input number {number} is not a Fizz and Buzz")

"""Enter the user input number to find Positive, Negative and Zero Nested if else codition"""
number=int(input("Enter the number = "))
if number>=0:
    if number>0:
        print(f"The user input number {number} is positive...")
    else:
        print(f"The user input number is {number}..")
else:
    print(f"The user input number {number} are negative")

# Loop 
"""An according to Data Analyst in python loop means which repeating something over the over until a particular 
condition are not satisfied is called Loop """
# while loop
""" during useing a loop the output is infinite time in terminal so you used ctr+c to stop them"""
i=1
while i<=10:
    print("Hello World!")
    i=i+1
    print("Done")
"""print 1 to 10 using while loop"""
i=1
while i<=10:
    print(i, end=" ")
    i=i+1
"""Write the number 1 to 20 only even number print"""
i=1
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i=i+1
"""Write the number 1 to 20 only even number print"""
i=1
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i=i+1
print("In this number 1 to 20 the even number")

"""Ask a number from the user. print the the number from 1 to input user number """
number=int(input("Enter the number = "))
i=1
while i<=number:
    print(i, end=" ")
    i=i+1
print(f"According to user input number {number} write to from 1") 

"""
Ask user input that starting and ending 
number to write the code within while loop
"""
S_num = int(input("Enter the starting number = "))
E_num = int(input("Enter the ending number = "))
# condition -1<------0------->+1
step = 1 if S_num <= E_num else -1
# i is Starting number 
i = S_num
while (i <= E_num if step == 1 else i >= E_num):
    print(i, end=" ")
    i += step

"""Calculate how many number are divisble by both 6 and 7 from 1 to 200 using while loop"""
i=1
count=0
while i<=200:
    if i%6==0 and i%7==0:
        print(i)
        count=count+1
    i=i+1
print("-"*30)
print(f"Total count number are divisble by both 6 and 7 from 1 to 200: {count}")
# For Loop
"""write the code 1 to 20 and add 5 """
for so in range (1, 21,5):
    print(so) 
"""write the code in 10 to 1"""
for i in range(10,0,-1):
    print(i, end=" ")
"""Ask the number from user. print all the numbers from 1 to that number """
User=int(input("Enter the number: "))
for i in range(1,User+1): #--------> User+1 because the exculsed
    print(i, end=" ")

"""Ask the number from a user input to 1"""
User=int(input("Enter the number:"))
for i in range(User,0,-1):
    print(i, end=" ")

"""Ask the number form a user Starting to ending print all number"""
Starting_User=int(input("Enter the starting number: "))
Ending_User= int(input("Enter the Ending number: "))
for i in range(Starting_User,Ending_User+1): #-------> Ending_User+1 is Exclude 
    print(i, end=" ")

"""Calculate the sum of all number from 1 to 10"""
Total=0
for i in range (1,10+1): # -------> using exclude for write 10+1
    Total=Total+i
print(f"Your answer is {Total}")

"""write the code from 1 to 100 and count how many number are divisible by a 7 """
count = 0
for i in range(1,100+1):
    if i%7==0:
        count=count+1
        print(i,end=" ")
print(f"the total number divide by 7 from 1 to 100 is = {count}")

"""Calculate how many number are divisble by both 6 and 7 from 1 to 200 using for loop"""
count=0
for i in range(1,200+1):
    if i%6==0 and i%7==0:
        print(f"{i} is divisble by both 6 and 7 ")
        count=count+1
print("-"*30)
print(f"Total Count {count}")

"""Write a program to calculate the sum of all numbers divisible by 4 from 20 to 50 using for loop """
count=0
for i in range (20,50+1):
    if i%4==0:
        print(f"{i} yes is divisble by 4 ")
        count=count+i
print("-"*30)
print(f"Total Sum {count}") 

"""Nested Loop:- means multiple loops as a form a onion shell """
"""
print the paertern
***** 
*****
*****
*****
*****
"""
# understand i as row form in matics
for i in range(1,6):
 # understand j as colum form in matrics  
      for j in range (1,6):
          print("*", end=" ")
      print("")
print("as you can see the output of *\n")
"""print a paertern 
12345
12345
12345
12345
12345"""
for i in range(1,6): # i is a row form in matrics
    for j in range (1,6): # j is a colum form of matrics
        print(j, end=" ")
    print()
print("As you can see the output\n")

"""print the 
54321
54321
54321
54321
54321"""
for i in range(5,0,-1): #no or row in matrics
    for j in range(5,0,-1):# no of column in matrics
        print(j,end=" ")
    print()
print("As you can see the Output\n")
"""print the output 
11111
22222
33333
44444
55555
"""
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()
print("As you can see the output\n")

"""write the user input n to pattern"""
user_r=int(input("Enter the how many row you want in matrics: "))
user_c=int(input("Enter the how many column you want in matrics: "))
for i in range(1,user_r+1):
    for j in range (1,user_c+1):
        print(i, end=" ")
    print()
print("As you see that the output\n")
"""Write the code to write the pertern
1
12
123
1234
12345
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("As you can see that output\n")
"""print this as a output 
1
22
333
4444
55555"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("As you can see that output\n")

"""print a pattern by using for loop
1
21
321
4321
54321
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
print("see this is the output\n")
"""print a parttern by using nested for loop
5
54
543
5432
54321
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()
print("see the output\n")
"""print a pattern by using nested for loop
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1  """
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i, end=" ")
    print()
print("See the output\n")

"""print this this parttern 
54321
5432
543
54
5
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()
print("as you can see the output\n")

"""print a parttern 
*****
****
***
**
*
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*", end=" ")
    print()
print("as you can see the output\n")

"""print a parttern
@@@@*
@@@**
@@***
@****
***** """
#according to me it's like a matric form of a parttern which make two triangle 
# so first triangle parten matric logic build
for i in range (1,6):
    for j in range (i,5):
        print("@",end=" ")
        
    for k in range(1,i+1):
        print("*",end=" ")
    
    print()
print("as you can see that the output\n")
"""print this parttern
             *
            ***
           *****
          *******
         *********
"""
n=5
for i in range(1,n+1):
    print(" " *(n-i)+"*"*(2*i-1))
print("as you can see that the output\n")    

"""  print the parttern
             *
            ***
           *****
          *******
         *********
          *******
           *****
            ***
             *
""" 
n=5
for i in range(1,n+1):
    print(" " *(n-i)+"*"*(2*i-1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print("as you can see this value\n")
       
# Operator 
"""
Arithmetic operator 
Assingment Operator 
Compersion Operator 
Logical Operator
Identity Operator 
Membership Operator 
Bitwise Operator 
Operator Precedence 
"""


# File Handling 
"""
File handling in Python is the process of creating, opening, reading, writing, 
updating, and deleting files on a storage device (like a hard drive) using 
a programming interface. It serves as a bridge between the program 
(which operates in volatile memory) and persistent storage, allowing 
data to be saved, retrieved, and managed after the program terminates.-
Json, {txt}:-> csv,excel, PDF, {Binary file}:-> png,mp3 and  JPG, exce and etc. is caleed File Handling.
"""
# Best practice approach
with open("C:\\Users\\DELL\\Downloads\\train.csv", "r") as file:
    content = file.read()
    print(content)# File is automatically closed here

# File Handling of PDF  Example 
import PyPDF2
path = "C:\\Users\\DELL\\Downloads\\Web Scraping with Python, 2nd Edition.pdf"
with open(path,"rb")as f:
    reader=PyPDF2.PdfReader(f)
    for page_num, page in enumerate(reader.pages):
        print(f"\n Reading:{page_num +1}")
        print(page.extract_text())

#
import pandas as pd



#Exception Handling
"""
Exception Handling in Python is a mechanism to manage runtime errors so 
that a program doesn't crash abruptly when it encounters an unexpected event. 
Instead of stopping execution, Python allows you to "catch" these errors, respond to them
"""
# important key word's
"""
(i) try: Wraps the "risky" code that might fail.
(ii)except: Executes only if an error occurs in the try block
(iii) else: Runs only if no exceptions occur in the try block.
(iv)finally: Always executes, regardless of whether an error occurred, typically for cleanup tasks like closing files
(v)raise: Manually triggers a specific exception when a custom condition is met.
"""
#real world  problem example:- like webapp, banking software, webscraping, automation buld during any project and etc 
import requests
from bs4 import BeautifulSoup
def get_web_data(url): # parametar pass
    try:
        # try: Attempting to connect to the data source
        response = requests.get(url, timeout=5)
        
        # raise: Check if the response is valid (e.g., status 200)
        response.raise_for_status() 
        
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error occurred: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except Exception as err:
        # except: Catch-all for unexpected errors
        return f"An unexpected error occurred: {err}"
    
    else:
        # else: Code runs only if the data was accessed successfully
        soup = BeautifulSoup(response.content, 'html.parser')
        page_title = soup.title.text if soup.title else "No Title Found"
        return f"Data Extracted: {page_title}"
        
    finally:
        # finally: Always runs, useful for logging or closing resources
        print("Scrape attempt completed.")

# Usage
result = get_web_data("https://www.example.com") # argument 
print(result)#recall the funcation 



# Module 
# Socket Programming 
# DataBase Conection 
# Multi Thrading 
# Pasword Managment 

#Funcation 
"""Definition of {Funcation}=> In Python, a function is a named, self-contained block of code that 
performs a specific task and only runs when it is called. Functions help you organize code, 
reduce repetition, and make your programs more modular and reusable is called funcation."""

# How to write a funcation in python ->
def Introduction():
 print("""Hi my name is Masood Rahman and i am 25 year old student and i was lookin a job as a post of python devloper 
my email id is : masoodrahman.0805@gmail.com
    """)
# Recal the funcation 
Introduction()# withiout argument
#Now we learn about How many type of funcation we can write 
"""
(i) Without parameter Without Return
(ii) With Parametar Without Return
(iii) Without Parametar With Return
(iv) With Parametar With Return
"""

def even_number():
    print("This is a Even number =>")
    for i in range(1,11):
        if i%2==0:
            print(i, end=" \n")      
even_number() #Without parameter Without Return Argument

"""Take a user end  two input and add the value to print by using funcation"""
def add():
    user_num_1=int(input("Enter the number: "))
    user_num_2=int(input("Enter the number: "))
    print(f"Total sum = {user_num_1 + user_num_2}")
add()
def sub():
    user_num_1=int(input("\nEnter the number: "))
    user_num_2=int(input("Enter the number: "))
    print(f"subtraction = {user_num_1 - user_num_2}\n")
    # Without parameter Without Return argument
sub()

"""Make a funcation to pass a parametar and argument with order"""                   
def Multiply(a,b):#Parametar
    print(f"a X b = {a*b}\n")
Multiply(10,10)# with parametar and with order Argument 

"""Write the code in funcation and pass the parametar and pass a argument by specific  Named parametar without order""" 
def percentage(English,Maths,Physics,Chemistry,Computer_Science):
    print(f"Your mark's in English = {English} ")
    print(f"Your mark's in Maths = {Maths}")
    print(f"Your mark's in Physics = {Physics}")
    print(f"Your mark's in Chemistry = {Chemistry}")
    print(f"Your mark's in Computer_Science = {Computer_Science}")
    Percentage= (English + Maths + Physics + Chemistry + Computer_Science) /500*100
    print("------*******-------")    
    print(f"Your percentage is {Percentage}%\n")
# Named parametar    
percentage(Maths=89, English=82, Physics=79, Computer_Science=82, Chemistry=76)

# Example :- Without Parametar Without Return
def Sum_maks():
    Maths=82
    Physics=84
    Chemistry=78
    Computer_Science=78
    English=89
    Total_sum = English + Maths + Physics + Chemistry + Computer_Science
    return Total_sum
print(f"The total marks are: {Sum_maks()}")

# Default Argument example
def Intro(Name="Guest",Age=0,Phone_no=None):
    return f"Name: {Name}, Age: {Age}, Phone: {Phone_no}"
print(f"\n{Intro(Name="Masood Rahman",Age=25)}\n")

"""write a funcation that accepts the integer and prints the tabel upto 10"""
def Tabel(Num):
    for i in range(1,11):
        print(f"{Num} x {i} = {i * Num}")
Tabel(5)

"""Write the user end funcation any num to write tabel upto 10""" 
def Usr_tabe(Num):
    Num=int(input("Enter the number to write the tabel: "))
    for i in range (1,11):
        print(f"{Num} x {i} = {Num *i}")
Usr_tabe(Num=0)

"""Write the funcation user end to find odd number or even numer"""
def Odd_Even():
    Num=int(input("Enter the number to check odd or even number: "))
    if Num % 2 ==0:
       return f" This number {Num} is Even"
    else:
       return f"This number {Num} is  is Odd"
print(Odd_Even())

"""Write the funcation that takes three numbers as parametar and prints the largest among them"""
def greater_num(Num_1,Num_2,Num_3):
    if Num_1>Num_2 and Num_1>Num_3:
        print(f"{Num_1} is greater number")
    elif Num_2>Num_1 and Num_2>Num_3:
        print(f"{Num_2} is greater number")
    else:
        print(f"{Num_3} is greater number")
greater_num(10,10.5,11)

"""Write the funcation to print prime number """
def prime_num(Num):
    Factor=0
    for i in range (1,Num+1):
        if Num%i==0:
            Factor+=1
    if Factor ==2:
       print("It is the Prime number:")
    else:
        print("It is a not a prime number: ")
prime_num(10)
prime_num(2)

"""Write the funcation to sum of a number at give list"""
def sum_of_list(numbers):#parametar
    total = 0
    for num in numbers:
        total = total + num
    print(f"Total sum: {total}")
    
    mean = total / len(numbers)
    print(f"Mean value: {mean}\n")
# recal funcation 
sum_of_list([1, 2, 3, 4, 5]) #list Argument
sum_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

"""Write the funcation that given string each chr repetead frequence"""
def chr_frequence(string): # Parametar 
    my_dic = dict()  # or use {}
    for ch in string:
        if ch not in my_dic:
            my_dic[ch] = 1 
        else:
            my_dic[ch] += 1
    return my_dic
# Recall the function
result = chr_frequence("Hi my name is Masood Rahman")#Argument
print(result)

"""Write the programe to find palindrome using funcation"""
def check_palindrome(string):
    if string==string[::-1]:
        print(f"Yes it's palindrome:->{string}")
    else:
        print(f"\nNo it's not palindrome:->{string}")
#recal the funcation
check_palindrome("noon")
check_palindrome("Fun")






