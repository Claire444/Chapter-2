def personal_info(): #excercise 1
    #personal info excepts no arguements
    #displays name, address, phone#, and college major
    print("Claire Pierson")
    print("12344 Square St., Wichita, KS, 67235")
    print("033-333-2323")
    print("farming")
    
def total_purchase(): #excerise 4
    #total purchase accepts no arguements
    #displays the subtotal of the sale, the amount of sales tax, and the total
    
    #collect prices of items
    first_item = float(input("Please enter a price for your first item:"))
    second_item = float(input("Please enter a price for your second item:"))
    third_item = float(input("Please enter a price for your third item:"))
    fourth_item = float(input("Please enter a price for your fourth item:"))
    fifth_item = float(input("Please enter a price for your fifth item:"))

    #collect subtotal before tax
    subtotal = int(first_item + second_item + third_item + fourth_item + fifth_item,)
    
    #calulate tax
    tax = float(format(subtotal * 0.07, ".2f"))
    
    #calculate total
    total = (subtotal + tax)
    
    #print subtotal, tax, and total
    print("Subtotal: $",format(subtotal,".2f"))
    print ("Tax: $", (format(tax, ".2f")))
    print ("Total: $", (format(total, ".2f")))
    
def distance_traveled(): #exercise 5
    #distance traveled accepts no arguements
    #asks for your speed, then calcualtes how long it will take you to travel a certain distance
    
    #collect speed
    mph = int(input("How fast are you driving?"))
    
    #calculate distance in 6, 10, 15, hours
    six_hours = int(mph * 6)
    ten_hours = int(mph * 10)
    fifteen_hours = int(mph * 15)
    
    #print distance
    print( "at", mph, "miles per hour you will travel", six_hours, "miles in 6 hours")
    print( "at", mph, "miles per hour you will travel", ten_hours, "miles in 10 hours")
    print( "at", mph, "miles per hour you will travel", fifteen_hours, "miles in 15 hours")
    
def sales_tax(): #exercise 6
    sale_amount = float(input("Enter the sale amount:"))
    state_tax = float(sale_amount * 0.025 )
    county_tax = float(sale_amount * 0.05)
    total_tax = (county_tax + state_tax)
    total_price = float(sale_amount + total_tax)
    
    print("Your purchase price was: $", format(total_price, ".2f"))
    print("Your state tax amount is: $", format(state_tax, ".2f"))
    print("Your county tax amount is: $", format(county_tax, ".2f"))
    print("Your total tax is $", format(total_tax, ".2f"))
    print("Your total sale is: $", format(total_price, ".2f"))
    
def tip_tax_total(): #exercise 8
    sale_amount = float(input("Please enter the sale amount:"))
    tip_amount = float(sale_amount * 0.18)
    tax_amount = float(sale_amount * 0.07)
    
    
    
    print("The sale was: $",format(sale_amount, ".2f"))
    print("The tip amount is: $", format(tip_amount, ".2f"))
    print("The sales tax amount is: $", format(tax_amount, ".2f"))
    print("The total bill is: $", format(sale_amount + tip_amount + tax_amount, ".2f"))
    
def temp_converter(): #exercise 9
    celsius_temp = float(input("Please enter the celsius degrees:"))
    fahrenheit_temp = ((celsius_temp * 1.8) + 32)
    print(celsius_temp, "degrees celsius is", fahrenheit_temp, "degrees fahrenheit")
    
def cookie_monster(): #exercise 10
    number_of_cookies = float(input("How many cookies do you want to make?"))
    one_cookie_sugar = float(.5)
    one_cookie_butter = float(.3333)
    one_cookie_flour = float(.9166)
                              
    total_cookie_sugar = float(number_of_cookies * one_cookie_sugar)
    total_cookie_butter = float(number_of_cookies * one_cookie_butter)
    total_cookie_flour = float(number_of_cookies * one_cookie_flour)
    
    cups_sugar = int(total_cookie_sugar//8)
    cups_butter = int(total_cookie_butter//8)
    cups_flour = int(total_cookie_flour//8)
    
    ounces_sugar = int(round(total_cookie_sugar % 8 - cups_sugar,0))
    ounces_butter =int(round(total_cookie_butter % 8 - cups_butter, 0))
    ounces_flour =int(round(total_cookie_flour % 8 - cups_butter, 0))
    
    print (cups_sugar,"cups", ounces_sugar, "ounces of sugar")
    print (cups_butter, "cups", ounces_butter, "ounces of butter")
    print (cups_flour, "cups", ounces_flour, "ounces of flour")
    
def class_demographics():
    females = float(input("Enter the number of females:"))
    males = float(input("Enter the number of males:"))
                   
    class_total = (females + males)
    percent_females = int((females/class_total) * 100)
    percent_males = int((males/class_total) * 100)
    
                   
    print("The class consists of ", percent_females, "% females and ",percent_males, "% males", sep='')              
    

import turtle
def tortuga_1(): #exercise 15
    #
    #draw light blue circle
    turtle.penup()
    turtle.goto(-175, 60)
    turtle.pendown()
    turtle.width(10)
    turtle.color("light blue")
    turtle.circle(75)
    
    #draw black circle
    turtle.penup()
    turtle.goto(0, 60)
    turtle.pendown()
    turtle.width(10)
    turtle.color("black")
    turtle.circle(75)
    
    #draw red circle
    turtle.penup()
    turtle.goto(175, 60)
    turtle.pendown()
    turtle.width(10)
    turtle.color("red")
    turtle.circle(75)
    
    #draw yellow circle
    turtle.penup()
    turtle.goto(-90, -30)
    turtle.pendown()
    turtle.width(10)
    turtle.color("yellow")
    turtle.circle(75)
    
    #draw green circle
    turtle.penup()
    turtle.goto(90, -30)
    turtle.pendown()
    turtle.width(10)
    turtle.color("green")
    turtle.circle(75)
    
    
def tortuga_2():
    turtle.penup()
    turtle.width(5)
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.goto(100,0)
    
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.goto(0,-100)
    
    turtle.penup()
    turtle.width(1)
    turtle.goto(50, 50)
    turtle.pendown()
    turtle.goto(-50,-50)
    
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.goto(50, -50)
    
    #North
    turtle.penup()
    turtle.goto(-8,115)
    turtle.write("N", font=("Arial", 20, "normal"))
    
    #south
    turtle.penup()
    turtle.goto(-8,-150)
    turtle.write("S", font=("Arial", 20, "normal"))
    
    #west
    turtle.penup()
    turtle.goto(-145, -8)
    turtle.write("W", font=("Arial", 20, "normal"))
    
    turtle.penup()
    turtle.goto(125,-8)
    turtle.write("E", font=("Arial", 20, "normal"))
    
                              

    
    
        
    

    
                              

    
    
        
    