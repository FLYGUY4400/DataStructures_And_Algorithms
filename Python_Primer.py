"""
@Dawson Bremner
@3/20/22
Python Primer Basics
"""
a = [1,2,3,4,5,6]

#While Loop
j = 0
while j < len(a) and a[j] != 3:
    j+=1;

print(j)

#Functions

#Function to find gpa
def compute_gpa(grades, points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
                  'C-' :1.67, 'D+' :1.33, 'D' :1.0, 'F':0.0}):
    num_courses = 0
    total_points = 0
    #Loop that computes gpa depending on grades
    for g in grades:
        if g in points:
            num_courses +=1
            total_points += points[g]
    return total_points / num_courses

#print(compute_gpa(['A','A','A','B']))

#Simple Input and Output
"""reply = input("Please enter values by x and y, seperated by spaces: "
              )
pieces = reply.split()
x = float(pieces[0])
y = float(pieces[1])
print(x)
print(y)
"""

#Files
#Use the open function
#'r' mode for reading
#'w' mode for writing (overwriting)
#'a' mode for appending

#Exception Handling
#Example

def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise TypeError('x cannot be negative')
    else:
        return (x**(1/2))

print(sqrt(9))

try:
    fp=open('sample.txt')
except IOError as e:
    print('Unable to open the file:',e)

#Iterators and Generators
"""
Iterator and Iterable 
"""
data = [1,2,3,4,5]
i = iter(data)

def factors(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k

factors(100)

#Python Conveniences

