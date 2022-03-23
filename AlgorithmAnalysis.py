#Algorithm Analysis

#Section 3.2

"""
The seven functions used in this book

1. The constant function f(n) = 3

2. The Logarithm Function
f(n) = log_b(n) for some constant b>1

3. The Linear Function

4. N-Log-N Function

5. Quadratic

6. Cubic Function

7. Polynomials

"""

#Section 3.2 Asymptotic Analysis
#We want to determine the runtime based on the component that grows the fastest

#Section 3.3 The "Big-Oh" Notation
""" 
f(n) \in O(g(n)) 
This is often used to characterize running times and space bounds 
We can ignore constant factors and lower-order terms 
"""

"""
Big-Omega Notation 
Greater than or equal. Opposite of big-oh notation 

"""

"""
Big Theta 
Two functions grow at the same rate up to constant factors 
c'g(n) <= f(n) <= c''g(n,  for n >= n0 
"""

#O(1) time is constant runtime that doesn't depend on n

"""
If we are trying to find the max of a list that is in random order, the expected number of
times we update the biggest is H_n = \sum_j=1^n 1/j 
This is known as the nth Harmonic Number 
"""

#Example of prefix averages

#A Quadratic-Time Algorithm
def prefix_average1(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total+=S[i]
        A[j] = total/(j+1)
    return A


def prefix_average2(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A

#Linear Time
def prefix_average3(S):
    n = len(S)
    A = [0]*n
    total = 0
    for j in range(n):
        total+=S[j]
        A[j] = total/(j+1)
    return A
#This runs in linear time because the prefix sum is not computed anew for each iteration of j

