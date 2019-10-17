# Integration-Project
# My name is Charles Spalding but I prefer to be called Patrick.
# This program is a basic estimator for Spalding Carpet Cleaners.
def carpetEstimate(startCarpet):


    additionalCarpet=input("Does user have additional carpet?(yes or no)")
    if additionalCarpet=="yes":
        feetOfCarpet=1
        totalCarpet=0
        print("When user would like to stop adding sections, enter the value 0.")
        while feetOfCarpet!=0:
            feetOfCarpet = float(input("Insert how much additional square feet of carpet.(Whole number/Decimal):"))
            totalCarpet+=feetOfCarpet
        totalCarpet=startCarpet+totalCarpet
    else:
        totalCarpet=startCarpet
    carpetPrice=input("Is it commercial or residential carpet?(commercial or residential):")
    commercialCarpet=float(.20)
    residentialCarpet=float(.30)
    if carpetPrice == "residential":
        totalCarpetPrice = totalCarpet * residentialCarpet
    else:
        totalCarpetPrice = totalCarpet * commercialCarpet
    return totalCarpetPrice

def tileEstimate(startTile):
    totalTile=0
    additionalTile=input("Does user have additional tile?(yes or no):")
    if additionalTile=="yes":
        feetOfTile=1
        print("When user would like to stop adding sections of rooms, enter the value 0.")
        while feetOfTile!=0:
            feetOfTile=float(input("Insert square feet of tile for this additional section.(Whole number/Decimal):"))
            totalTile+=feetOfTile
        totalTile=totalTile+startTile
    else:
        totalTile=startTile
    tilePrice=input("Is it commercial or residential tile?(commercial or residential):")
    residentialTile=float(.65)
    commercialTile=float(.55)
    if tilePrice == "residential":
        totalTilePrice = totalTile * residentialTile
    else:
        totalTilePrice = totalTile * commercialTile
    return totalTilePrice

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
    #I know it's bad practice to use global, I just got stumped trying to use parameter instead.
    global totalUpholsteryPrice
    if biggerThanThat == "yes":
        biggerCushions = int(input("How many bottom cushions does it have?:"))
        totalUpholsteryPrice=(numberOfSofas*85)+(numberOfLoveSeats*65)+(numberOfRecliners*45)+(20*biggerCushions  +25)+\
                             (numberOfDiningChairs*10)+(numberOfPillows*5)+(numberOfOttoman*15)
    else:
        totalUpholsteryPrice=(numberOfSofas*85)+(numberOfLoveSeats*65)+(numberOfRecliners*45)+\
                               (numberOfDiningChairs*10)+(numberOfPillows*5)+(numberOfOttoman*15)


print("Welcome to the basic estimate program for Spalding Carpet Cleaners!")
print("Cleaners measure areas of room at a time, then multiply that by a price seen fit for labor/size of job.")
carpetChoice=input("Would user like to measure carpet?(yes or no):")
if carpetChoice=="yes":
    initialCarpet = float(input("How many square feet of carpet would user like cleaned?(Whole number/integer):"))
    priceOfCarpet=carpetEstimate(initialCarpet)
    tileChoice=input("Are there also areas of tile and grout?(yes or no):")
    if tileChoice=="yes":
        initialTile=float(input("How many square feet of tile would user like cleaned?(Whole number/integer):"))
        priceOfTile=tileEstimate(initialTile)
        upholsteryChoice=input("Would user like to estimate upholstery as well?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            totalEstimate=(priceOfCarpet+priceOfTile+totalUpholsteryPrice)
            print("Your total estimate price for carpet, tile, and upholstery is:","$"+
                  format(totalEstimate,".2f"), "dollars.")
        else:
            print("Your total estimate for carpet and tile is:","$"+format(priceOfCarpet+priceOfTile,".2f"),"dollars.")
    else:
        upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your total estimate for carpet and upholstery is:","$"+format(totalUpholsteryPrice+priceOfCarpet,".2f"),"dollars.")
        else:
            print("Your total estimate price is:","$"+format(priceOfCarpet,".2f"),"dollars.")
elif carpetChoice!="yes":
    tileChoice=input("Would user like to measure tile and grout?(yes or no):")
    if tileChoice=="yes":
        initialTile = float(input("How many square feet of tile would user like cleaned?(Whole number/integer):"))
        priceOfTile = tileEstimate(initialTile)
        upholsteryChoice=input("Would user also like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your estimate price for tile and upholstery is:","$"+format(totalUpholsteryPrice+priceOfTile,".2f"),"dollars.")
        else:
            print("Your estimate price for tile is:", "$" + format(totalTilePrice, ".2f"), "dollars.")
    else:
        upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
        if upholsteryChoice=="yes":
            upholsteryEstimate()
            print("Your estimate price for upholstery is:", "$" + format(totalUpholsteryPrice, ".2f"), "dollars.")
        else:
            print("I apologize for being no use.")
            print("Have a nice day!")

#else:
    #upholsteryChoice=input("Would user like to measure upholstery?(yes or no):")
    #if upholsteryChoice=="yes":
        #upholsteryEstimate()
        #print("Your estimate price for upholstery is:", "$" + format(totalUpholsteryPrice, ".2f"), "dollars.")
    #else:
        #print("I apologize for being no use.")
        #print("Have a nice day!")
