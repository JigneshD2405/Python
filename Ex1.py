'''#celsius----- Farenheit

c= input('Enter the Celsius: ');
c=float(c);

F= (c*9/5)+32;

print('The farenheit is = ' , F);


#farenheit ---- Celsius

F= input('Enter FeranHit : ')
f=float(F)
c= (f-32)*5/9

print('The celsius is ',c)


#simple Interest

p= input('P:')
r=input('r:')
n=input('n:')

p=float(p)
r=float(r)
n=float(n)


SI=(p*r*n)/100

print("Simple Interest is :" ,SI)
'''


#print(max(1,56,30,45))

#print(min(1,56,30,45))


#print(abs(-20))

#print(pow(6,2))

'''a= int(input('Enter the value of A:' ))

if (a>5):
    print('A is greater')

print("None")

Marks=int(input('Enter the Marks:'))

if (Marks>=40):
    print('Passed')
else:
    print('Failed')
print('Thank You')'''
'''
age = int(input('Please Enter Your Age: '))

if (age>18):
    print("Yes You can vote")
else:
    print('No,You Cannot vote')
print("Thank You")

operand_1 = int(input('Enter the Operand_1:'))
operand_2 = int(input('Enter the Operand_2:'))
operator=input("Please Enter the opertor(+,-,/,*):")


if (operator=='+'):
    print(operand_1+operand_2)
elif (operator=='-'):
    print(operand_1-operand_2)
elif(operator=='*'):
    print(operand_1*operand_2)
elif(operator=='/'):
    print(operand_1/operand_2)
else:
    print('None')
print('Thank You')



n=list(range(1,101,5))
print(n)




for i in range(1,10):
    print()


count= 1
while (count<=5):
    print(count)
    count +=1
'''


#x= ['Jignesh','Pradipbhai,Dudharejiya']
#for i in range(1,11,2):
 #   print(i)

'''count=10
while count>=1:
    print(count)
    count-=1'''
'''
def jignesh():
    print("Hello")
    print("World")


jignesh()
def Hello_Jignesh():
    str1='Hello'
    str2=" python"
    print(str1+str2)

Hello_Jignesh()


def add(a,b):
    a=int(input("Enter the value of A:"))
    b = int(input("Enter the value of B:"))
    c=a+b
    return c


ans=add(10,20)
print(ans)


def add(a,b):
    return a+b

def square(x):
    return x*x

ans=square(add(2,5))

print(ans)
'''
#import math
#print(math.pi)

'''
from math import *
print(pi)

def python():
    print('python',n)
    python()

python()


def factorial(n=int(input('Enter the number:'))):
    if (n<2):
        return 1
    else:
        return n *(factorial (n-1))


result=print(factorial())


import  calendar
    c=calendar.month(1991, 3)
    print(c)

try:
    a=5
    b=0
    print(a/b)
except IndentationError:
    print("Hello")
finally:
    print("World")


my_dict={1:'J',2:'I',3:'G',4:'N',5:'E',6:'S',7:'H'}
print(my_dict[])


my_dic={'J':1,'I':2,'G':3,'N':4,'E':5,'S':6,'H':7}
print(my_dic)


dictionary={'a':'apple','b':'Ball','c':'Cat','d':'Dog'}

dictionary['e']='Elephant'
#print(dictionary)
#del(dictionary['c'])
#print(dictionary)
#print('b' in dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.get('g','G is NOt found'))




list=['cricket','Football']
list1=['kabbadi','kho-kho']
print('cricket' in list)
print(list+list1)

#list=[1,2,3]

#print(list*2)

list=['Cobro','CHetu','Maru','Bhuro','Rahul','Baapu']

list.append('Tako')
list.extend(['utpal','sagar'])
print(list)


list=['Cobro', 'CHetu', 'Maru', 'Bhuro', 'Rahul', 'Baapu', 'Tako', 'utpal', 'sagar']

#list.remove('sagar')


del list[0:2]
print(list)

list.clear()
print(list)'''


#l=[245,28,62,229,99,115,131]

#l.pop(6)
#print(l)

#l.insert(2,199)
#print(l)

#l.sort()
#print(l)

#l.reverse()
#print(l)


#print(l.index(62))


#numbers=[10,12,14,16,18,20,22,24,26,28,30]

#print(numbers[0:11:2])

#x=[i**2 for i in range(11) if i%2!=0]
#print(x)
'''
set={1,2,3,4,5,6}
set.add(7)
#print(set)
#set.remove(6)
print(set)
print(6 in set)




set1={1,2,3,4,5,6,7}
set2={1,3,5,6}

#print(set1 & set2)

#print(set1.union(set2))


print(set2.issubset(set1))'''


#a= 'jIGNesh'
#print(a.capitalize())
#print(a.upper())
#print(a.lower())

'''
a='10'
print(a.isnumeric())'''

#a='Mike is good boy'
#print(a.startswith('Mike'))
#print(a.endswith('boy'))
#print(a.replace('Mike','Jack'))
#print(a.replace('is','are'))
#print(a.find('good'))
#print(a.lstrip())
#print(a.rstrip())
#print(a.splitlines())

'''
name= input('Enter your name :')
num = len(name)*3
print("Hello {}, Your lucky Number is {}".format(name,num))
'''
'''
example= 'Hello World'
string='{} I love Python'.format(example)

print(string)
'''
'''
jignesh='Apple'
Jayshree= 'Ball'
Aruna='Cat'

print('{2} {1} {0}'.format(jignesh,Jayshree,Aruna))


price = 120
with_tax =120+20

print("Price: rs {:.2f}  and Price with tax : Rs {:.2f}".format(price,with_tax))
'''


#numbers =(1,3,2,4,1,5)
#print(numbers[4])

#tup1= (1, 'Mike', 2.5,'Jignesh')
#tup2=("Hey ,Bro HOw are You",2)
#print(tup1+tup2)
#print(len(tup2))
'''
num= (1,3,2,54,32,4,245,657,132421234)
#print(sorted(num))
print(num.index(54))


fun=lambda a,b :  a+b
print(fun(2,3))'''


'''
def even(a):
    return a%2==0

num = range(1,10)

ans = set(filter(even,num))
print(ans)


ans=list(filter(lambda a:a%2==0,range(101)))
print(ans)




def squares():

    n=1
    while n<=5:
        square= n ** 2
        yield square
        n+=1

value=squares()
print(value.__next__())
print(next(value))



class car:
    brand = 'BMW'
    type='SUV'
    color='Black'

jig=car()

print(jig.color.capitalize())
print(jig.color.capitalize())



class counting:
    n=0
    def cnt(s):
        s.n+=1
        print("Counted",s.n)

c=counting()

for i in range(6):
    c.cnt()



class const_dest:
    x=0
    def car(self):
        print("Hii")
    def __init__(j,color,type):
        j.color =color
        j.type =type
        print("Constructor")

    def __del__(j):
        print("Destructor")

cd=const_dest('black','suv')

print(cd.car())
print(cd.type)
print(cd.color)
'''
'''
class Jignesh:
    x=0
    name=""

    def jig(j,k):
        j.name= k
        print("Hello ",k)

class Football_Fans(Jignesh):
    pts=0

    def pts(self):
        print(self.name,"Score")

f=Football_Fans("Jig")
f.pts()
'''
'''
j=Jignesh()
j.jig("Jignesh")


class A:

    def State_1(self):
        print("State_1 Present")

    def State_2(self):
        print("State_3 Present")

    def State_3(self):
        print("State_3 Present")


class B():

    def State_4(self):
        print("State_4 Present")

    def State_5(self):
        print("State_5 Present")

class C(A,B):

    def State_6(self):
        print("State_6 Present")

    def State_7(self):
        print("State_7 Present")

c=C()
c.State_7()


class simple:

    def __init__(self):
        self.value_1=1
        self.value_2=2
    def __A1_(self):
        print("Apple")

    def _B1_(self):
        print("Ball")

s=simple()

 print(dir(s))
        

import  re

pattern = "Apple"

if re.match(pattern,"apple"):
    print("True")
else :
    print("False")
'''


import re

Jignesh= "Hi Jignesh How are You 24"

pattern="\S"
print(re.findall(pattern,Jignesh,flags=0))







































































