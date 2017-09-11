import sys

def calculation (abv, oz, con, cost):
    abv = abv/100
    oz = oz * con
    return (3/abv) * (cost/oz)

def operation():
    try:
        abv = float(input("What is the ABV percentage? "))
        oz = input("How many ounces are in a single container? Enter 'L' for litres. ")
        if oz.lower() == 'l':
            print("ml/1000 = litres")
            li = float(input("How many litres are in a single container? "))
            oz = float(li * 33.8135)
        else:
            oz = float(oz)
        con = int(input("How many containers are in the unit? "))
        cost = float(input("How much is the unit? $"))
    except ValueError:
        operation()
    total = calculation(abv, oz, con, cost)
    total = round(total, 2)
    print("3 ounces of pure alcohol from this unit costs ${}".format(float(total)))
    end = input("What would you like to do now? Enter Q to quit or any key to reset. ")
    if end.lower() == 'q':
        print("Good Bye!")
        sys.exit()
    else:
        operation()

operation()
