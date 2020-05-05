''' Question 1:-Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.'''

print("1) 2000 to 3200 which is Divided by 7 but don't print the value which is multiple of 5:-\n")
x = []
for i in range(2000 ,3200+1):
    if (i % 7 == 0) and (i % 5 != 0):
       x.append(str(i))

print(','.join(x))

''' Question 2:- Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.'''

print("\n")
FirstName = input("Enter Fisrt Name:-")
LastName = input("Enter Last Name:-")
Result = LastName+" "+FirstName
print("2) ",Result)

''' Question 3:- Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3 '''

print("\n","Diameter solution:-")
D = int(input("enter the value of Diameter of Sphere:- "))
R = D/2
P = 22/7
V = 4/3*P*R**3
print("3) Volume of Sphere :-",V,"cm^3")

''' Question 4:-Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
print("4) Pattern Program")
for row in range(1,6):
    for column in range(0,row):
        print("*",end=" ")
    print("")
for row in range(6+1,0,-1):
    for column in range(1,row):
        print("*",end=" ")
    print("")

''' Question 5:-Write a Python program to reverse a word after accepting the input from the user.'''

Input = str(input("\n 5)  Enter the name Which you wanna reverse:-"))
Output = Input[::-1]
print("Reverse String:-",Output)


''' Question 6:-Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.'''

num = input("6) Enter the number with comma separator :-")
List_num = num.split(",")
print(List_num)

# Question 7:- Write a Python Program to print the given string in the format specified in the sample output.

orignal_string = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into \na SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all \nits citizens\n"
x = "WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a".expandtabs()
y = "\n\t\t SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC".expandtabs()
z = "\n\t\t and to secure to all its citizens".expandtabs()
print("7) Orignail Data :-\n",orignal_string)
print("Modified Data :-\n",x,y,z)
