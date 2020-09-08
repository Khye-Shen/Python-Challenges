def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i

    return f


def series(A, X, n):

    nFact = factorial(n)


    for i in range(0, n + 1):

        niFact = factorial(n - i)
        iFact = factorial(i)


        aPow = pow(A, n - i)
        xPow = pow(X, i)

        print (int((nFact * aPow * xPow) /
                   (niFact * iFact)), end = " ")

    # Driver Code


A = 3
X = 4
n = 5
series(A, X, n) 