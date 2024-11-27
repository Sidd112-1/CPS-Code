'''a=int(input("Enter a number: "))
if a%7==0:
    print("Number is divisble by 7")
else:
    print("Number is not divisible by 7")'''



'''b=int(input("Enter a number:"))
if b%7==0:
    print("Number is divisible by 7")
    if b%5==0:
        print("Number is divisible by 5")
        print('Number is divisible by both 7 and 5')
    else:
        print('Number is divisibly by 7 but not 5')
else:
    print("Number is not divisible by both 7 and 5")'''

'''p=int(input("Enter a number:"))
q=int(input("Enter a number:"))
print(" 1. SUM")
print("2. DIFFERENCE")
print("3. PRODUCT")
print("4. DIVISION")
O= int(input("Choose any of the above option(number only):"))
if O==1:
    sum=p+q
    print('Sum=',sum)
elif O==2:
    diff=p-q
    print("Difference=",diff)
elif O==3:
    product=p*q
    print("Product=",product)
elif O==4:
    if q!=0:
        div=p/q
        print("Division=",div)
    else:
        print('Division not possible')
else:
    print('Choose a valid option')



x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
Sum=x+y+z
print('Sum of three numbers=',Sum)



S=int(input("Enter a number:"))
Area_SQ=S**2
print('Area of Square=',Area_SQ)



length=int(input("Enter a number:"))
breadth=int(input("Enter a number:"))
Area= length*breadth
print("Area of Rectangle=",Area)



radius=int(input("Enter a number:"))
Area_Circle=3.14*(radius**2)
print("Area of Cricle=",Area_Circle)



a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
D= (b**2)-(4*a*c)
print("Discriminant=", D)'''


#monthly_pay=no_hours*rate*weeks
#dist_delhi_mumbai
#int_hrs_min
#speed_dist_time

'''No_hrs=int(input("Enter number of hours worked in a week:"))
Rate=int(input("Enter rate per week"))
Weeks=int(input("Enter no of weeks worked"))
Monthly_Pay= No_hrs*Rate*Weeks
print('Monthly_Pay of employee=',Monthly_Pay)



dist=float(input("Enter distance between Mumbai and Delhi"))
Speed=60
Time=dist/Speed
print("Journey Time(in hr):",Time)
Fuel_hr=100
Fuel_Cost=Fuel_hr*Time
print('Fuel Cost=',Fuel_cost)



sec=int(input("Give a number(in seconds):"))
min=sec/60
print("Number in minutes=",min)
hr= min/60
print("Number in hours=",hr)



distance=int(input("Enter distance:"))
time=int(input("Enter time"))
sp=distance/time
print("Speed=",sp)'''

'''h=int(input("Enter a number:"))
if h<0:
    print("Number is negative")
elif h==0:
    print("Number is 0")
elif h>0:
    print("Number is positive")
else:
    print("Enter a valid number")


x=int(input("Enter a number"))
if x%2==0:
    print("number is even")
elif x%2!=0:
    print("number is odd")
else:
    print("Enter a valid number")


y=int(input("Enter your age:"))
if y>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


p=int(input("Enter a number"))
q=int(input("Enter a number"))
r=int(input("Enter a number"))
if p>q and p>r:
    print("p is largest")
elif q>p and q>r:
    print("q is largest")
elif r>p and r>q:
    print("r is largest")


avg_marks=float(input("Enter your average marks"))
if avg_marks>=80:
    print("Your grade is A")
elif avg_marks>=60 and avg_marks<=80:
    print("Your grade is B")
elif avg_marks>=40 and avg_marks<=60:
    print("Your grade is C")
elif avg_marks<=40:
    print("Your grade is F")


points=0
while True:
    char=input("Enter a character:")
    if len(char)>1:
        print()
        print("Please enter only 1 character!!")
        print()
    else:
        break

if char in 'aeiouAEIOU':
    points=5
elif int(char).isdigit():
    points=10
print("You're points are",points)'''


f=input("Enter a letter:")
if f.isupper():
    print("Letter is uppercase")
elif f.islower():
    print("Letter is lowercase")
else:
    print("Enter a valid letter")
    

#Method 2
f=input("Enter a letter:")
if ord(f) in range(97,123):
    print("letter is lowercase")
elif ord(f) in range(65,91):
    print("letter is uppercase")
else:
    print("Enter valid character")


'''a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
D=(b**2)-(4*a*c)
p=0
if D>0:
    print("It has real roots")
    p=p+20
elif D==0:
    print("It has equal roots")
    p=p+0
elif type(D)==complex:
    print("It has imaginary roots")
    p=p+10
print("Points=",p)


Weight=float(input("Enter your weight(in kg):"))
Height=float(input("Enter your height(in m):"))
BMI=Weight/(Height**2)
if BMI<18.5:
    print("You are underweight")
elif BMI>18.5 and BMI<24.9:
    print("You are normal weight")
else:
    print("You are overweight")


x=int(input("Enter a coordinate for x:"))
y=int(input("Enter a coordinate for y"))
if x>0 and y>0:
    print("Point lies in first quadrant")
elif x>0 and y<0:
    print("Point lies in second quadrant")
elif x<0 and y<0:
    print("Point lies in third quadrant")
elif x<0 and y>0:
    print("Point lies in fourth quadrant")
else:
    print("Enter a valid point")


year=int(input("Enter a year"))
if year%4==0:
    print("Year is leap year")
else:
    print("Year is not leap year")


Amount=float(input("Enter amount spent:"))
if Amount in range(0,1001):
    print("Your Discount is 5%")
elif Amount in range(1001,5001):
    print("Your Discount is 10%")
elif Amount in range(5001,10001):
    print("Discount is 20%")
else:
    print("Enter valid Amount")'''
