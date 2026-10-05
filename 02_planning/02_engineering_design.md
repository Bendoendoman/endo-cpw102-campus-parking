# Engineering Design

**Project:** Campus Parking Helper  
**Team members:**  Benjamin Endo
**Date:** 9/28/2026

## Problem Summary
Currently there is no simple and easy way for staff and visitors to calculate the cost of parking, which can lead to mistakes especially when it comes to parking for partial hours

## Proposed solution
A simple application that can run in the terminal that can calculate the cost of parking based on the number of hours parked.


## Technical design


### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_
Should have 1 input float
May have 1 more input float for people who have already parked for x hours and want to park for longer 
if that is the case may also have 1 input booleans to determine if they have already parked for some time or not 

### Processing
_What will the program do with the data? What calculations will it perform?_ 
Should multiply the float (hours) by 2.00

### Output
_What will the program return or print to the user?_
Should return a string that contains a message
i.e. : "Your estimated cost is X amount"

### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_
costCalculator: Should have the input code for the float and should return the string "Your estimated cost is X amount"

questions: Should have all the logic for the text queries and should implement costCalculator at the appropriate time 

## Example interaction

```text 
Have you already been parked for an amount of time? (type Y for yes or N for no and then press enter)

User input: Y

Program output: Do you plan to park for a longer amount of time, or do you want to figure out how much it will cost for the current amount of time parked? (please type either "Longer" or "Current" then press enter)

User input: Current

Program output: please type the current amount of time you have parked for in the format hours_minutes (i.e. 6_24)[then press enter]

User input: 5_22 

//(5+0.367)*2
a

Program output: Your estimated cost is 10.73$
```

## Implementation plan

1. program questions
2. program costCalculator
3. format the responses correctly

