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
a = [2,212,24,534,26,63,65]

def odds(a):

    for j in range(1,len(a)):
        if a[0]*a[j] % 2 == 1:
            print('The numbers ' + str(a[0]) + ' and ' + str(a[j]) + ' work')
            quit()
        elif a[0]*a[j] % 2 == 0 and j != len(a)+1:
            continue
        else:
            print("No")
print(odds(a))