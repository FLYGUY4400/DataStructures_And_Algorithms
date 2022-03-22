"""
Write a short Python function, is multiple(n, m), that takes two integer values and returns True
if n is a multiple of m, that is, n = mi for some integer i,
and False otherwise.
"""
def multiple(n,m):
    if(m % n==0):
        return True
    else:
        return False

print(multiple(5,10))
print(multiple(7,24))

""" 
Write a short Python function 
that takes a positive integer n and returns 
the sum of the squares of all the positive integers smaller than n.
"""
def smaller_Squares(n):
    sum = 0
    i = 1
    while (i < n):
        sum += i*i
        i += 1
    return sum

print(smaller_Squares(4))

#Problem1.9
for i in range(50,80,10):
    print(i)

#C.1.14
a = [1,212,24,534,26,63,65]

def odd_count(n):
    odd_count = 0
    i = 0
    while i < len(n):
        if n[i] % 2 == 1:
            odd_count += 1
            i += 1
        else:
            i += 1
    print(odd_count)

    if odd_count >= 2:
        print("Yes, there are at least two odds")
    else:
        print("No")

odd_count([1,2,3])


