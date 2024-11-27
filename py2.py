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
print("You're points are",points)


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


a=int(input("Enter a number"))
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
    print("Enter valid Amount")


def greet(**kwargs):
    name=kwargs.get("name","World")
    age=kwargs.get("age",30)
    print(f"Hello,{name}!You're {age}years old")
greet(name="John",age=25)


for i in range(5,7):
    for j in range(1,11):
        print(i*j)'''


'''import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print(" I'm thinking of a number between 1 to 100.")
    target_number=random.randint(1,100)
    attempts=0

    while True:
        guess=input("Enter your guess:")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess=int(guess)
        attempts+=1
        if guess< target_number:
            print("Too low! Try again")
        elif guess> target_number:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You guessed the number is {attempts} attempts")
            break
guess_the_number()


#Rock Paper Scissors
import random
def rock_paper_scissors():
    choices=["rock","paper","scissors"]
    score=0
    print("Welcome to Rock,Paper,Scissors!")

    while True:
        user_choice=input("Enter 'rock','paper', or 'scissors'(or 'quit to exit):").lower()
        if user_choice== 'quit':
            print(f"Thanks for playing! Your total score is: {score}")
            break
        elif user_choice not in choices:
            print("Invalid choice, try again")
            continue

        computer_choice=random.choice(choices)
        print(f"Computer chose {computer_choice}")

        if user_choice==computer_choice:
            print("It's a tie!")
        elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice == "scissors" and computer_choice == "paper") or  (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score=score+1
        else:
            print("You lose!")
rock_paper_scissors()

# Magic 8-Ball
import random
def magic_8_ball():
    responses=["Yes,definitely","No way!","Maybe...","Ask again later","It is certain.","Very doubtful.","Outlook no so good.","Signs point to yes."]
    print("Welcome to Magic 8-Ball!")

    while True:
        question=input("Ask a yes/no question (or 'quit' to exit):")
        if question.lower()=='quit':
            break
        print(random.choice(responses))
magic_8_ball()

#constructor is a special method whose name is same as class name and is used for object creation
thistuple=tuple(("Amrita"))
print(type(thistuple))

x.intersection_update(y) #set
# symmetric_difference_update will pick uncommon elements
# symmetric_difference''' 

pos=-1
def search(list,n):
    i=0
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    return False
list=[2,6,5,4,7,8,1]
n=7
if search(list,n):
    print("The element is present in the list at index",pos)
else:
    print("The element is not present in the list at index",pos)

