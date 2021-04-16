

"""
This program is trying to determine which payment option will result in more money. 
The first optio is 100 dollars per day for 10 days. The second option is 1 dollar the first day,
2 dollars the second day, and will be doubled each day for 10 days. 
There will be two funtions to calculate the total payment for both options.  
funtion1 will calculate the amount for option 1. function2 will calculate the amount for option2.

function1 will output 100 * 10 days. 
funtion2 will loop 10 times and each time the pay amount will double and then the amount will be added to the total. 

the amount is the same, we output to the user "Option 1 and Option 2 pays the same"
if option 1 is better, we output to the user "Option 1 is better"
if option 2 is better, we output to the user "Option 2 is better"
"""

"""
# option1
    return 100 * 10

# option2
amount = 1
list1 = []
loop 10 times
    add amount to list1
    amount *= 2
sum = sum of all items in loop
    return amount

# main
    var1 = option1
    var2 = option2

    if var1 = var2
        "Option 1 and Option 2 pays the same"
    if var1 > var2
        "Option 1 is better"
    else
        "Option 2 is better"


main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total


def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    if var1 > var2:
        answer = "Option 1 is better"
    else:
        answer = "Option 2 is better"
    print(answer)

main()