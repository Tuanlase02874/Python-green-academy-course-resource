def displayRange(lower, upper):
    """Outputs the numbers from lower through upper."""
    while lower <= upper:
        print(lower)
        lower = lower + 1


def recursiveDisplayRange(lower, upper):
    """Outputs the numbers from lower through upper."""
    if lower <= upper:
        print(lower)
        lower = lower + 1
        recursiveDisplayRange(lower + 1, upper)
    else:
        
        print("lower") 
print("recursiveDisplayRange")
recursiveDisplayRange(lower=4, upper=8)

print("displayRange")
displayRange(lower=4, upper=8)

