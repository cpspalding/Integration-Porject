# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.
# This program is a basic estimator for Spalding Carpet Cleaners.
print("Welcome to my basic estimating program for Spalding Carpet Cleaners!")
carpet = float(input("How many cents per a square foot?(Decimal):"))
feet = int(input("Insert how many square feet of carpet.(Whole number):"))
price=carpet*feet
print("Your estimate price is:","$"+format(price,".2f"), "dollars.")
