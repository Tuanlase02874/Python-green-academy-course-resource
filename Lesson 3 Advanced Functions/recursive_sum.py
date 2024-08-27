
def sum(lower, upper, margin):
    for x in range(margin):
        print(" ", end="")  # Print spaces without a newline
    print(lower, upper)  # Print lower and upper

    if lower > upper:
        for x in range(margin):
            print(" ", end="")  # Print spaces without a newline
        print(0)  # Print 0 if lower is greater than upper
        return 0
    else:
        result = lower + sum(lower + 1, upper, margin + 2)  # Recursive call
        for x in range(margin):
            print(" ", end="")  # Print spaces without a newline
        print(result)  # Print result after recursive call
        return result



def recursive_sum(lower, upper, margin):
    # Python 3 requires print as a function
    for x in range(margin):
        print(" ", end="")  # end="" ensures no newline is added after printing the space
    print(lower, upper)  # prints the lower and upper values
    
    if lower > upper:
        for x in range(margin):
            print(" ", end="")  # prints margin spaces
        print(0)  # prints 0 if lower is greater than upper
        return 0
    else:
        result = lower + sum(lower + 1, upper, margin + 2)  # recursive call with incremented lower and margin
        for x in range(margin):
            print(" ", end="")  # prints margin spaces
        print(result)  # prints the result after recursion unwinds
        return result

    
print("sum")
sum(lower=1, upper=5, margin=2)