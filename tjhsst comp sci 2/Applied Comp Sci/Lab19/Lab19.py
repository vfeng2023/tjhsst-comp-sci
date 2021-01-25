# Name: Vivian Feng and Shriya Muthukumar

# import necessary functions (import * from math)
import math

#increment each value of n individually
nums = open('lab19.txt', 'w')
# for n in range(1, 2):
n = 1
totalSeq1 = 0
totalSeq2 = 0
while n <= 30:

    if n%2 == 1:
        totalSeq1 += 1.0/(2*n-1)
    else:
        totalSeq1-= 1.0/(2*n-1)

    totalSeq2 += 1.0/(n**2)
    piSeq1 = totalSeq1 * 4
    piSeq2 = math.sqrt(totalSeq2*6)
    nums.write(str(n) + " " + str(piSeq1) + " " + str(piSeq2) + " " + str(math.pi) + "\n")
    n+= 1




nums.close()