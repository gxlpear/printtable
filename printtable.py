def get_multtable(number, limit):
    """
    Returns a list with multiplication table for number
    from 1 to limit
    """
    result =  []
    for i in range(1, limit+1):
        result.append(i * number)
    return result


def multtable(number, limit):
    """
    Prints multiplication table for number
    from 1 to limit

    >>> multtable(7, 3)
    7
    14
    21
    """
    for i in range(1, limit+1):
        print(i * number)



def powertable(power, limit):
    """
    Prints power table from 1 to limit for input power

    >>> powertable(2, 5)
    1
    4
    9
    16
    25
    """
    for n in range(1, limit + 1):
        result =  n **power
        print(result)

def newpowertable(power, n):
    while n > 0:
        result = n **power
        n = n - 1
        print(result)

if __name__ == "__main__":
    multtable(7, 10)
    powertable(2, 4)
    newpowertable(2,4)

