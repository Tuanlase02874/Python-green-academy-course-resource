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
        print("DEBUG result:", result)
    return result

print(summation(1,4))

print(summation(50,100))