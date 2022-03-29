#Chapter 4, Recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

""" 
Binary Search 
"""
""" 
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary search(data, target, low, mid-1)
    else:
        return binary search(data, target, mid + 1, high)

"""
""" 
Linear Recursion: When each invocation of the body makes at most 
one recursive call 
Binary Recursion: When a function makes two recursive calls 
Multiple Recursion: When a function makes more than two recursion calls 
"""

def linearSum(S,n):
    if n == 0:
        return 0
    else:
        return linearSum(S,n-1) + S[n-1]

#Problem R-4.1
def recursiveMax(n):
    if len(n) == 1:
        return n[0]
    elif n[len(n)-1] > recursiveMax(n[:len(n)-1]):
        return n[len(n)-1]
    else:
        return recursiveMax(n[:len(n)-1])

print(recursiveMax([1,5,123,55,123,1,56,23,5,32,12344]))

#Problem C-4.16
def isPalindrome(n):
    if len(n) == 1:
        return True
    elif len(n) == 2:
        if n[0] == n[1]:
            return True
        else:
            return False
    else:
        if n[0] == n[len(n)-1]:
            return isPalindrome(n[1:len(n)-1])
        else:
            return False



print(isPalindrome('Dawson'))
print(isPalindrome('racecar'))
print(isPalindrome('gohangasalamiimalasagnahog'))


def recursiveHarmonics(n):
    harmonic = 0
    if n == 1:
        harmonic = 1
    else:
        harmonic = 1/n + recursiveHarmonics(n-1)
    return harmonic

print(recursiveHarmonics(1))
print(recursiveHarmonics(3))
print(recursiveHarmonics(6))
print(recursiveHarmonics(8))

def minAndMax(n):
    min_n = n[0]
    max_n = n[0]
    if len(n) == 1:
        min_n = n[0]
        max_n = n[0]
    elif n[len(n)-1] > recursiveMax(n[:len(n)-1]):
        max_n = n[len(n)-1]
    elif n[len(n)-1] < recursiveMax(n[:len(n)-1]):
        min_n = n[len(n)-1]
    else:
        min_n = minAndMax(n[len(n)-1])
        max_n = minAndMax(n[len(n)-1])
    return min_n, max_n
print(minAndMax([4,5,123,55,123,1,56,23,5,32,12344]))


#Problem C-4.11
def elementUniqueness(a):
    if len(a) == 1:
        return True
    elif a[0] in a[1:]:
        return False
    else:
        return elementUniqueness(a[1:])


print(elementUniqueness([1,2,3,4,5,6,7]))
print(elementUniqueness([1,2,2,3,4,5,6,7]))
print(elementUniqueness([1,2,3,4,5,6,7,7]))
print(elementUniqueness([1,1]))

