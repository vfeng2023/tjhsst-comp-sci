#Name: Karthik and Vivian
#Date:10/2/2019

from random import random
matchnum = []

#finds proportion of matches of first edge vs final direction
for n in range(1,26):
   matches = 0
  
   for trial in range(10000):
      m = 2*n +1
      j = n+1
      times = 0
      while	1<=j<=m:
         r = random()
         if	r < 0.5:
            j+=1
         else:
            j-=1
         if (j == m or j==1) and times == 0:
            firstEdge = j
            times += 1
      if firstEdge == m and j == m+1:
         matches +=1
         
      elif firstEdge == 1 and j == 0:
         matches +=1
      
   matchnum.append((100.0*matches)/10000)


md = open('matchedge.txt','w')

for i in range(1,26):
   md.write(str(i) + " " + str(matchnum[i-1]) + '\n')
   
md.close()