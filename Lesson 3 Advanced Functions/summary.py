def summation(lower, upper):
    """
        Arguments: A lower bound and an upper bound
        Returns: the sum of the numbers from lower through
        upper
    """
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
        #print("DEBUG result:", result)
    return result

def recursive_summation(lower, upper):
    if upper < lower:
        return 0
    return upper + recursive_summation(lower, upper - 1)

print(summation(1,4))
print("recursive_summation")
print(recursive_summation(1,4))

#print(summation(50,100))