def comment_example():
    #comment example receives no arguements
    #it explains how to create a function header
    #and outputs or returns "hello world!"
    print('Hello World')

def program2_1(): #apostrophe output
    print ('Kate Austen')
    print ('123 Full Circle Drive')
    print ('asheville, NC 28899')

def program2_2(): #double quote output
    print ("Kate Austen")
    print ("123 Circle Drive")
    print ("Asheville, Nc 28899")
    
def program2_3(): #apostrophe test
    print ("don't fear!")
    print ("I'm here!")
    
def program2_4():
    print ('Your assignment is to read "Hamlet" by tomorrow')
    
def program2_5(): #double quote output
    #this function displays a person's name and address
    print ("Kate Austen")
    print ("123 Circle Drive")
    print ("Asheville, Nc 28899")
    
def program2_6(): 
    #display name
    print ('Kate Austen')
    #display address
    print ('123 Full Circle Drive')
    #display the city, state, and ZIP
    print ('asheville, NC 28899')
    
def program2_7(): #variable demo 1
    #demonstrates variable
    print("I am staying in room")
    room = 503
    print (room)
    
def program2_8(): #variable demo 2
    #demonstrates 2 variables
    top_speed = 160
    distance = 300
    #displays variables
    print ('The top speed is')
    print (top_speed)
    print ('The distance traveled is')
    print (distance)
    
def program2_9(): #variable demo 3
    #this program demonstrates outputting a variable
    room = 503
    print ('i am staying in room number', room)
    
def program2_10():
    dollars = 2.75
    print('I have', dollars,'in my account!')
    
    dollars = 99.95
    
    
    
def program2_11():
    #variables for name
    first_name = 'kathryn'
    last_name = 'marino'
    
    #display name
    print (first_name, last_name)

    
def program2_12():
    first_name = input("enter your first name: ")
    
    last_name = input('enter your last name: ')
    
    print('hello', first_name, last_name)
    
def program2_13(): #variable demo 
    #collect name
    first_name = input("What is your name?")
    #collect age
    age = input("what is your age?")
    #collect income
    income = input("what is your income?")
    #display name, age, income
    print("Here is the data you entered:")
    print("name:", first_name)
    print("Age:", age)
    print("income:", float(income))
    
def program2_14():
    #set money varaibles
    income = (2400)
    
    bonus = (1300)
    #display total income
    print("Your pay is:", float(income + bonus))
def sale_price():
    #get item's original price
    og_price = float(input("Enter the item's original price:"))
    #calc amount of discount
    discount = (float(og_price) * float(.2))
    #calc discount price
    discount_price = (og_price - discount)
    #display
    
#syntax = format(<variable><precision><type>)
    
    print("The sale price is:", discount_price)
    
def get_average(): #program2_16
    first_test_score = float(input("enter the first test score:"))
    
    second_test_score = float(input("enter the second test score:"))
                              
    third_test_score = float(input("enter the third test score:"))
                             
    total_score = (first_test_score + second_test_score + third_test_score)
                             
    average = (total_score / 3)
    
    print("The average score is:", average)
    
def program2_17(): #time converter
    total_seconds = float(input("Enter the number of seconds:"))
    
    #get number of hours
    hours = total_seconds // 3600
    
    #get remaining minutes
    minutes = (total_seconds //60) % 60
    
    #get the number of remaining seconds
    seconds = total_seconds % 60
                          
    #outputs
    print("here is the time in hours, minutes, seconds.")
    print("Hours:", hours)
    print("minutes:", minutes)
    print("seconds:", seconds)
    
def program2_18():
    desired_value = float(input('Enter the desired future value:'))
    rate = float(input("Enter the annual interest rate:"))
    years = int(input('Enter the number of years the money will grow:'))
    present_value = desired_value/(1.0 + rate)**years
    print("you will need to deposit $", format(present_value, '.2f'), sep='')
    
def program2_19():
    amount_due = 5000
    monthly_payment = (amount_due/12)
    print("the monthly payment is", monthly_payment)
    
def program2_20():
    amount_due = 5000
    monthly_payment = (amount_due/12)
    print("the monthly payment is", format(monthly_payment, '.2f'))
    
def program2_21():
    monthly_pay = 5000
    annual_pay = (monthly_pay*12)
    print("Your annual pay is $", format(annual_pay, ',.2f'), sep='')
    
def program2_22():
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999
    
    print(format(num1, '7.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '7.2f'))
    print(format(num4, '7.2f'))
    print(format(num5, '7.2f'))
    print(format(num6, '7.2f'))
    
import turtle
def orion():
    #setup turtle
    turtle,setup(500,600)
    turtle.penup()
    turtle.hideturtle()
    
    left_shoulder_x = -70
    left_shoulder_y = 200
    
    right_shoulder_x = 80
    right_shoulder_y = 100
    
    left_belstar_x = -40
    left_belstar_x = -20
    
    
    
    
    
    
    