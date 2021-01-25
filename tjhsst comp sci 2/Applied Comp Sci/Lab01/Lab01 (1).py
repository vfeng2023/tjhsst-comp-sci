##Name: Karthik and Vivian
#Date: 10/1/2019


from random import random

n=5
m=2*n+1
j=n+1
steps=0

k=1

while k<=m:
   if k==j:
      print 'X',
   elif k==n+1:
      print '|',
   else:
      print '-',
   k+=1
print
      


while 1 <=j<=m:
   if random()<0.5:
      j+=1
      steps+=1
      k=1
      while k<=m:
         if k==j:
            print 'X',
         elif k==n+1:
            print '|',
         else:
            print '-',
         k+=1
      print
      
   else:
      j-=1
      steps+=1
      k=1
      while k<=m:
         if k==j:
            print 'X',
         elif k==n+1:
            print '|',
         else:
            print '-',
         k+=1
      print
print "The number of Steps is ",steps
      

   



  