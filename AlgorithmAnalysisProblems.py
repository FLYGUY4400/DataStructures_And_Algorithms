#AA Problems

#Problem C.3.35

"""
Suppose that we are able to sort n numbers in O(nlogn) time.
First, we sort all three of the sets, each in O(nlogn) time.

Then we have
a = {a1,a2,...,an}
b = {b1,b2,...,bn}
c = {c1,c2,...,cn}

Because sets cannot have duplicate values, we concatenate the three lists using and then
see if there is a subset of three values that are all the same which takes O(n) time.
"""

#C-3.41

a = [2,2,3,67,233,654,12,78,35]
#We want to run this on n time, (n=8) in this case

#We want this to find the min and max on at most 12 comparisons


