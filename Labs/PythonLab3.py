# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.
# RQ1
def doubletime(i,n):
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    "*** YOUR CODE HERE ***"

    for j in range(0, n):
            i = i * 2
    return i

# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    "*** YOUR CODE HERE ***"
    lst = []

    for i in range(0, round(n/3) + 1):
        if(n > 0):
            lst.append(n)
            n -= 3
    return sum(lst)
	
# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    "*** YOUR CODE HERE ***"
    lst = [1]

    for i in range(2, n + 1):
        if lst[-1] % 2 == 0:
            lst.append((3 / 2) * lst[-1])
        else:
            lst.append((3 / 2) * (lst[-1] + 1))
    
    return int(lst[-1])

# RQ4
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    lst = [[1] * n for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            lst[i][j] = lst[i - 1][j] + lst[i][j - 1]

    return lst[-1][-1]

import doctest
if __name__ == "__main__":
	doctest.testmod(verbose=True)
