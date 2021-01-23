from math import e, factorial
import numpy as np

fac = np.vectorize(factorial)

def e_x(x, terms=10): # https://www.notion.so/skinetics/Installing-Numpy-Guide-c593cd18554d428087352306c3bf2c1f#07ee8f39460842cca163e73eaeaf89a7
    n = np.arange(terms) # Calculate the entire Maclaurin series
    return np.sum((x ** n) / fac(n)) # return series

if __name__ == "__main__":
    print("Actual:", e ** 3) # e from standard library math
    print("N (terms\tMaclaurin\tError")

    for n in range(1, 14):
        maclaurin = e_x(3, terms=n)
        print(f"{n}\t\t{maclaurin:.03f}\t\t{e**3 - maclaurin:.03f}")