#Name: ... and Vivan
#Date: 10/2/2019
from random	import random


n = int(raw_input("Value of n: "))

trials = []

for trial in range(10000):
   m = 2*n +1
   j = n+1
   steps	= 0
   while	1<=j<=m:
      r = random()
      if	r < 0.5:
         j+=1
      else:
         j-=1
      steps	+=	1
   trials.append(steps)
   
avg = (1.0*sum(trials))/10000

print "The average is ",avg
      
	



