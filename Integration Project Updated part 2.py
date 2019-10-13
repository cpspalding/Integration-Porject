# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.
# This program is a basic estimator for Spalding Carpet Cleaners.
print("Welcome to my basic estimate program for Spalding Carpet Cleaners!")
choice1=input("Would user like to measure carpet?(yes or no):")
if choice1=="yes":
    print("Cleaners measure areas sections at a time, then multiply that by a price seen fit for labor/size of job.")
    print("When user would like to stop adding sections of areas, enter the value 0.")
    feetOfCarpet=1
    totalFeet=0
    while feetOfCarpet>0:
        feetOfCarpet = float(input("Insert how many square feet of carpet for this section.(Whole number/Decimal):"))
        totalFeet+=feetOfCarpet
    pricePerFoot=input("Is it commercial or residential carpet?:")
    commercialCarpet=float(.20)
    residentialCarpet=float(.30)
    if pricePerFoot == "commercial":
        totalCarpetPrice=totalFeet*commercialCarpet
    else:
        totalCarpetPrice=totalFeet*residentialCarpet
    #print("Your estimate price for carpet is:","$"+format(totalCarpetPrice,".2f"), "dollars.")
choice2=input("Are there areas of tile and grout?(yes or no):")
if choice2=="yes":
    print("When user would like to stop adding sections of areas, enter the value 0 as input.")
    feetOfTile = 1
    totalTile=0
    while feetOfTile>0:
        feetOfTile=float(input("Insert how many square feet of tile for this section.(Whole number/Decimal):"))
        totalTile+=feetOfTile
    tilePrice=(input("Is it commercial or residential tile?:"))
    residentialTile=float(.65)
    commercialTile=float(.55)
    if tilePrice=="residential":
        totalTilePrice=totalTile*residentialTile
    else:
        totalTilePrice=totalTile*commercialTile
    total=totalCarpetPrice+totalTilePrice
    print("Your total estimate price is:","$"+format(total,".2f"),"dollars.")
else:
    print("Your total estimate price is:","$"+format(totalCarpetPrice,'.2f'),"dollars.")