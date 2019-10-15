# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.
# This program is a basic estimator for Spalding Carpet Cleaners.
def carpetEstimate():
    print("Cleaners measure areas of room at a time, then multiply that by a price seen fit for labor/size of job.")
    print("When user would like to stop adding sections of areas, enter the value 0.")
    feetOfCarpet=1
    totalFeet=0
    while feetOfCarpet>0:
        feetOfCarpet = float(input("Insert how many square feet of carpet for this section.(Whole number/Decimal):"))
        totalFeet+=feetOfCarpet
    pricePerFoot=input("Is it commercial or residential carpet?(commercial or residential):")
    commercialCarpet=float(.20)
    residentialCarpet=float(.30)
    if pricePerFoot == "commercial":
        totalCarpetPrice=totalFeet*commercialCarpet
    else:
        totalCarpetPrice=totalFeet*residentialCarpet

def tileEstimate():
    print("When user would like to stop adding sections of rooms, enter the value 0 as input.")
    feetOfTile = 1
    totalTile=0
    while feetOfTile>0:
        feetOfTile=float(input("Insert how many square feet of tile for this section.(Whole number/Decimal):"))
        totalTile+=feetOfTile
    tilePrice=(input("Is it commercial or residential tile?(commercial or residential):"))
    residentialTile=float(.65)
    commercialTile=float(.55)
    if tilePrice=="residential":
        totalTilePrice=totalTile*residentialTile
    else:
        totalTilePrice=totalTile*commercialTile

def upholsteryEstimate():
    numberOfSofas = int(input("How many sofas would user like cleaned?(3 bottom cushions)(Enter whole number or 0):"))
    numberOfLoveSeats = int(input("How many love seats would user like cleaned?"
                                  "(2 bottom cushions)(Enter whole number or 0):"))
    numberOfRecliners = int(input("How many recliners would user like cleaned?/"
                                  "(1 bottom cushion)(Enter whole number or 0):"))
    numberOfPillows = int(input("How many pillows would user like cleaned?(Enter whole number or 0):"))
    numberOfOttoman = int(input("How many ottoman would user like cleaned?(Enter whole number or 0):"))
    numberOfDiningChairs = int(input("How many dining room chairs would user like cleaned?(Enter whole number or 0):"))
    biggerThanThat = input("Do you have any couches larger than previously described?(yes or no):")
    if biggerThanThat == "yes":
        biggerCushions = int(input("How many bottom cushions does it have?:"))
        totalUpholsteryPrice=(numberOfSofas*85)+(numberOfLoveSeats*65)+(numberOfRecliners*45)+(20*biggerCushions  +25)+\
                             (numberOfDiningChairs*10)+(numberOfPillows*5)+(numberOfOttoman*15)
    else:
        totalUpholsteryPrice=(numberOfSofas*85)+(numberOfLoveSeats*65)+(numberOfRecliners*45)+\
                               (numberOfDiningChairs*10)+(numberOfPillows*5)+(numberOfOttoman*15)

print("Welcome to the basic estimate program for Spalding Carpet Cleaners!")
carpetChoice=input("Would user like to measure carpet?(yes or no):")
if carpetChoice=="yes":
    carpetEstimate()
    tileChoice=input("Are there also areas of tile and grout?(yes or no):")
    if tileChoice=="yes":
        tileEstimate()
        upholsteryChoice=input("Would user also like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your total estimate price for carpet, tile, and upholstery is:","$"+format(totalCarpetPrice+totalTilePrice+totalUpholsteryPrice,".2f"), "dollars.")
        else:
            print("Your total estimate price is:","$"+format(totalCarpetPrice+totalTilePrice,".2f"),"dollars.")
    else:
        upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your total estimate price is:","$"+format(totalUpholsteryPrice+totalCarpetPrice,".2f"),"dollars.")
        else:
            print("Your total estimate price is:","$"+format(totalCarpetPrice,".2f"),"dollars.")
elif carpetChoice!="yes":
    tileChoice=input("Would user like to measure tile and grout?(yes or no):")
    if tileChoice=="yes":
        tileEstimate()
        upholsteryChoice=input("Would user also like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your estimate price for tile and upholstery is:","$"+format(totalUpholsteryPrice+totalTilePrice,".2f"),"dollars.")
        else:
            print("Your estimate price for tile is:", "$" + format(totalTilePrice, ".2f"), "dollars.")
    else:
        upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your estimate price for upholstery is:", "$" + format(totalUpholsteryPrice, ".2f"), "dollars.")
        else:
            print("I apologize for being no use.")
else:
    upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
    if upholsteryChoice=="yes":
        upholsteryEstimate()
        print("Your estimate price for upholstery is:", "$" + format(totalUpholsteryPrice, ".2f"), "dollars.")
    else:
        print("I apologize for being no use.")
