#Name: Karthik and Vivian
#Date:10/2/2019

from random import random
matchnum = []

# finds proportion of first step vs final direction matches

for n in range(1,26):
   matches = 0
  
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
         if steps==0:
            veryFirstStep=(j-(n+1))
         steps	+=	1
         
      if veryFirstStep== 1 and j==m+1:
         matches+=1
      if veryFirstStep==-1 and j==0:
         matches+=1
      
   matchnum.append((100.0*matches)/10000)


md = open('matchdirection.txt','w')

for i in range(1,26):
   md.write(str(i) + " " + str(matchnum[i-1]) + '\n')
   
md.close()