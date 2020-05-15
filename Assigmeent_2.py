# 1.Write List comprehensions to produce the following Lists

L1 = ['A', 'C', 'A', 'D', 'G', 'I','L','D']
L2 = ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
L3 = ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']

Li1 = [i for i in L1]
print("List 1:-",Li1)
Li2 = [i for i in L2]
print("List 2:-",Li2)
Li3 = [i for i in L3]
print("List 3:-",Li3)

L4 = [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
Li4 = [i for i in L4]
print("List 4:-",Li4)
L5 = [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
Li5 = [i for i in L5]
print("List 5:-",Li5)
L6 = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
Li6 = [i for i in L6]
print("List 6:-",Li6)



# 2. Implement a function longestWord() that takes a list of words and returns the longest one.
def LongestWord():
    l = ['Computer', 'Science', 'Information']
    longstring = max(l, key=len)
    print("Elements Present in a list:-",l)
    print("This is a Longest String in given list:-",longstring)
LongestWord()


#3. Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
#      a vowel, False otherwise.

def Vowel(Char):

    Input = Char.lower()
    if (Input == 'a' or Input == 'e' or Input == 'i'or Input =='o' or Input == 'u'):
        print(True)
    else:
        print(False)
Char = input("Enter the Char to check it's Vowel or not:-")
Vowel(Char)


# 4.  Write a Python program using function concept that maps list of words into a list of integers
#    representing the lengths of the corresponding words .
#    Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#    Here 2,3 and 4 are the lengths of the words in the list

def LenWord():
    l = ['ashish','sonu','ajay']
    l2 = []
    l3 = []
    print("Orignal List:-",l)
    for i in l:
        l2 = len(i)
        l2 = l3.append(l2)
    print("Length of String present in List:-",l3)
LenWord()


#   5. Write a Python program to implement your own myfilter() function which works exactly like
#       Python's built-in function filter()
def filter1(fun, coll):
    results = []
    print("Called..")
    for i in coll:
        #stat = fun(i)
        if fun(i):
            results.append(i)
    return results


even = lambda x: x % 2 == 0
j = filter(even, range(1,11))

for k in j:
    print(k)


# 6. Write a Python program to implement your own myreduce() function which works exactly like
#        Python's built-in function reduce()

def do_sum(x, y):
    return x+y

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first


print(my_reduce(do_sum, [1,2,3,4]))


# 7. Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula.
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5


class Triangle:
    def Area_tri(self, s, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = s
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area
A = Triangle()
a = int(input("enter the value of A:-"))
b = int(input("enter the value of B:-"))
c = int(input("enter the value of C:-"))
s = int(input("enter the value of S:-"))
print(A.Area_tri(a,b,c,s))