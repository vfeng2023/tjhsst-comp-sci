#Name: ... and Vivian
#Date: 10/04/2019


from random import random

inp = int(raw_input("Enter 1 or 2: "))
# 1 gives the percent of Trials where First Step matches Final Direction

# 2 gives the percent of Trials where First Edge matches Final Direction
    
  


if inp == 1:
   matchnum = []
   
   
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
            steps += 1
   
         if veryFirstStep== 1 and j==m+1:
               matches+=1
         if veryFirstStep==-1 and j==0:
               matches+=1  
      
      
      matchnum.append((100.0*matches)/10000)
     
   md = open('matchdirection.txt','w')
   
   for i in range(1,26):
      md.write(str(i) + " "+str(matchnum[i-1]) + '\n')
      
   md.close()
   
   print 'Option 1 selected'

elif inp== 2:
   matchnum = []

   
   for n in range(1,26):
      matches = 0
      for trial in range(10000):
         m = 2*n +1
         j = n+1
         times	= 0
         while	1<=j<=m:
            r = random()
            if	r < 0.5:
               j+=1
            else:
               j-=1
            if (j==m or j ==1) and (times == 0):
               firstEdge = j
               times += 1
   
         if firstEdge == m and j==m+1:
               matches+=1
         
         if firstEdge==1 and j==0:
               matches+=1  
      matchnum.append((100.0*matches)/10000)
     
   md = open('matchEdge.txt','w')
   
   for i in range(1,26):
      md.write(str(i) + " "+str(matchnum[i-1]) + '\n')
      
   md.close()
   
   print 'Option 2 selected'
