catch = input()

def main():
    questions()

def costCalculator(numHours,numMinutes):
    return float((numMinutes/60)+numHours)*2
def questions():
    print("Hello, this program is for calculating the cost of parking at Clover Park University")
    print("Have you already been parked for an amount of time? (type Y for yes or N for no and then press enter)", catch)
    if(catch == "Y"):
        print("Do you plan to park for a longer amount of time, or do you want to figure out how much it will cost for the current amount of time parked? (please type either \"Longer\" or \"Current\" then press enter", catch)
        if(catch == "Current"):
            print("Please type the current amount of time you have parked for in the format hours_minutes (i.e. 6_24)[then press enter]",catch)
        elif(catch == "Longer"):
            print("Please type how much longer you plan on parking for, and how long you have currently parked for in the format hours_minutes (i.e(i.e. 6_24))")
            #catches both number separately and then adds them together, need to figure out how to break apart strings into different variables
            longer = catch
            costCalculator(numHours,numMinutes)
            current = catch
            costCalculator(numHours,numMinutes)
            
    elif(catch == "N"):
        print("How long are you planning to park for?", catch)

main()



    