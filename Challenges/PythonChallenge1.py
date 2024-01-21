# take 2 input numbers and make them a fraction n/d
# then separate them to only have a 1 in the numerator

def egypt(n, d):
    result = []

    while n != 0:
        unitFraction = -(-d // n)  # Ceiling division to find the largest unit fraction
        result.append(f"1/{unitFraction}")
        n = n * unitFraction - d
        d = d * unitFraction
    print(" + ".join(result))

egypt(3, 4)
egypt(11, 12)
egypt(123, 124)
egypt(103, 104)
