"""
4/3/2022
Working on Arrays
"""

#Notes
""" 
Referential Arrays: Store values of object references 
A shallow copy is a copy of a new list from an existing one (immutable objects in the list) 
A deep copy is a new list with new elements (mutable objects in the list) 

Compact Arrays: Array that stores the bits that represent the primary data


"""

#List Comprehension
squares = [k*k for k in range(1,5)]
print(squares)
""" 
from collections import Counter

if __name__ == "__main__":
    # Number of shoes 
    X = int(input())

    # List of all shoe sizes in shop 
    # Use list comprehension 
    my_list = [i for i in map(int, input().split())]

    # Convert list to counter 
    counter_list = Counter(my_list)
    earnings = 0
    # Do this for each purchase 
    N = int(input())
    while N > 0:
        a, b = map(int, input().split())
        if counter_list[a] != 0:
            earnings += b
            counter_list[a] -= 1
            N -= 1
        else:
            N -= 1
    print(earnings)
"""

#Insertion Sort
def insertionSort(A):
    for k in range(1,len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

#Multidimensional List
#Use a list comprehension

data = [[1]*3 for j in range(3)]

print(data)



