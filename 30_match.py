# !Match :-
# *The "Match" statement is used to perform different action based on different conditions.

# ?The Python Match Statement:-
# Inserted of writing many 'if...elif...else' statements, we can use the 'match' statement.
# The 'match' statement selects one of many code blocks to executed.
""" syntax:

    match expression:
        case x:
            code block
        case y:
            code block
"""

# example:
day = int(input("enter day num : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
        
# example:
day = int(input("enter day num : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("wrog input!!")
                
# example:
day = int(input("enter day num : "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today's a weekday")
    case 6 | 7:
        print("I love weekends!")