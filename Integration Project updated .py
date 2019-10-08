# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.
# This program is a basic estimator for Spalding Carpet Cleaners.
print("Welcome to my basic estimate program for Spalding Carpet Cleaners!")
print("Cleaners measure areas sections at a time, then multiply that by a price seen fit for labor/size.")
print("When user would like to stop adding sections of areas, enter the value 0.")
feetOfCarpet=1
totalFeet=0
while feetOfCarpet>0:
    feetOfCarpet = float(input("Insert how many square feet of carpet for this section.(Whole number/Decimal):"))
    totalFeet+=feetOfCarpet
pricePerFoot=float(input("How many cents per square foot of carpet?(Decimal):"))
totalCarpetPrice=totalFeet*pricePerFoot
#print("Your estimate price for carpet is:","$"+format(total,".2f"), "dollars.")
choice=input("Is there areas of tile as well?(yes or no):")
feetOfTile=1
if choice=="yes":
    print("When user would like to stop adding sections of areas, enter the value 0.")
    totalTile=0
    while feetOfTile>0:
        feetOfTile=float(input("Insert how many square feet of tile for this section.(Whole number/Decimal):"))
        totalTile+=feetOfTile
    tilePrice=float(input("How much cents per square foot of tile?(Decimal):"))
    totalTilePrice=totalTile*tilePrice
    total=totalCarpetPrice+totalTilePrice
    print("Your estimate price is:","$"+format(total,".2f"),"dollars.")
else:
    print("Your estimate price for carpet is:","$"+format(totalCarpetPrice,".2f"), "dollars.")

