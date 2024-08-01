#10/7/24-wed
"""print ("hello world")
print ('how are you?')
print (23)
print("hello\nworld")
print('world'+'2')
print ('world '*3)
print(2+3)
print("2"+'3')"""


#11/7/24-thur

#Arithmetic operations
"""print(4+2) #add
print(4-2) #sub
print(4*2) #multiply
print(4/2) #division
print(15//2) #floor division
print(4%2) #modulo (to get remainder)
print(2**2) #exponential
print (4**(1/2)) #root operation"""

#Boolean operator

"""print(7<2)
print(7>2)
print(7<=2)
print(7>=7)
print(7!=7)
print(3+2==5) #comparison operator"""

#variables - used for temporary storage

"""x=2
print(x)
print(x+10)
y=5
print(y)
print(id(y))#(to get address)
y=3
print(y) #variables can be reassigned
print(id(y))
print(x+y)

x=30
y=50
z=x+y
s=(y**x)
a=(y*x)
print("addition :",z)
print("power is",s )
print("multiplication is",a)"""

#type conversion
"""a=10
b=5
c=float(a)+float(b)
print("result is",c)"""

#input from user
"""a=int(input("enter a number:"))
b=int(input("enter 2nd number:"))
c=a+b
print("the result is",c)"""

#12/07/24 - friday

#swapping
"""a=5
b=10
print("before swapping a,b : ",a,b)
temp=a
a=b
b=temp
print("after swapping a,b : ",a,b)"""

#swapping without third variable
'''a=10
b=50
print("before swapping a,b : ",a,b)
a,b=b,a
print("after swapping a,b : " ,a,b)'''

#conditional statements

#1.if condition
#syntax
'''if condition:
      statement'''

'''if 10>5:
    print("10 is greater")
print("finish")

if "hello"=="yellow":
    print("good morning")
print("finish")'''

#2.ladder if
'''if condition:
      statement
      if condition:
         statement
         if condition:
            statement'''

'''a=5
if a>2:
    print("good")
    if a>1:
        print("morning")
        if a>8:
            print("afternoon")
print("Thankyou")'''

#3.if else
'''if condition:
      statement
   else:
       statement'''

'''a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
if a==b:
    print("square")
else:
    print("rectangle")'''

"""a=int(input("enter a number : "))
if a%2==0:
    print("even")
else:
    print("odd")"""

#17/07/24-tuesday

#4.if else ladder

'''if condition:
      statement
    else:
      statement(if condition)'''

# to check whether a letter is vowel or not

'''a=input("enter an alphabet : ")
vowel="aeiouAEIOU"
if a in vowel:
    print("letter is a vowel")
else:
    print("not a vowel")'''


#elif

'''color=input("enter a colour : ")
if color=="red":
    print("color is red")
elif color=="green":
    print("color is green")
elif color=="blue":
    print("color is blue")
else:
    print("not a RGB colour")'''

'''#greatest among 3 numbers
a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
c=int(input("enter 3rd number : "))
if a>b and a>c:
    print("1st number is greater")
elif b>a and b>c:
    print("2nd number is greatest")
elif c>a and c>b:
    print("3rd number is greatest")'''
      
