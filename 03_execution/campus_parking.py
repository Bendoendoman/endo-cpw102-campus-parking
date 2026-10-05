import sys


def main():
    while True:
        try:
            questions()
            break
        except ValueError,TypeError,RuntimeError:
            print("wrong input try again")
            questions()
            sys.exit()

"""
commented out bc is un needed i think
why did no one tell me that input() always returns a string, so it wont return an error bc its comparing 2 strings anyways
Still let me learn some pretty cool code about sys.exit() and typeError vs valueError

def valueCheck(valueToBeChecked,expectedValue):
    if (valueToBeChecked == expectedValue):
        return valueToBeChecked
    elif (valueToBeChecked != expectedValue):
        return False

def isNumber(possibleNumber):
    try:
        float(possibleNumber)
        return True
    except ValueError:
        return False
        
"""

def costCalculator(time):
    x = time.index("_")
    numHours = time[0:x]
    print(numHours)
    numMinutes = time[x+1:]
    print(numMinutes)
    return round((((float(numMinutes)/60)+(float(numHours)))*2),2)
    #didn't understand exactly how input() worked, fixed it later


def questions():
    print("Hello, this program is for calculating the cost of parking at Clover Park University")
    print("Have you already been parked for an amount of time? (type Y for yes or N for no and then press enter)")
    catch = input()
    
    if(catch == "Y"):
        print("Do you plan to park for a longer amount of time, or do you want to figure out how much it will cost for the current amount of time parked? (please type either \"Longer\" or \"Current\" then press enter")
        catch = input()
        
        if(catch == "Current"):
            print("Please type the current amount of time you have parked for in the format hours_minutes (i.e. 6_24)[then press enter]")
            catch = input()
            print("Your estimated cost is", costCalculator(catch),"$")

            
        elif(catch == "Longer"):
            print("Please type how much longer you plan on parking for, press enter, then enter how long you have currently parked for, in the format hours_minutes (i.e(i.e. 6_24))")
            #catches both number separately and then adds them together, need to figure out how to break apart strings into different variables
            catch = input() 
            longer = catch
            try:
                longer = costCalculator(longer)
            except ValueError, TypeError:
                print("that is not a valid input, please try again")
                questions()
                sys.exit()
                
            catch = input()
            current = catch
            try:
                current = costCalculator(current)
            except ValueError, TypeError:
                print("that is not a valid input, please try again")
                questions()
                sys.exit()
            
            total = longer+current
            print("Your estimated cost is", round(total,2),"$")
        else:
            print("that is not a valid input, please try again")
            questions()
            sys.exit()
            
    elif(catch == "N"):
        print("How long are you planning to park for? Please type in the format hours_minutes (i.e. 6_24), then press enter")
        catch = input()
        
        print("Your estimated cost is", costCalculator(catch),"$")   
        
    else:
        print("that is not a valid input, please try again")
        questions()
        sys.exit()
        
main()