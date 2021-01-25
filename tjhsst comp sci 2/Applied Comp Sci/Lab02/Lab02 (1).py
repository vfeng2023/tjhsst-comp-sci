from random import random
import matplotlib.pyplot as plt


x = [number for number in range(1,26)]
step_avgs = []
for n in range(1,26):
   trials = []
   for trial in range(10000):
      m = 2*n +1
      j = n+1
      steps = 0
      while 1<=j<=m:
         r = random()
         if r < 0.5:
            j+=1
         else:
            j-=1
         steps +=1
      trials.append(steps)
   avg = (1.0*sum(trials))/10000
   step_avgs.append(avg)


plt.plot(x,step_avgs,"bo")
plt.title('n vs. Average Number of Steps',fontsize=24)
plt.ylabel("Average Number of Steps",fontsize=14)
plt.xlabel("n",fontsize=14)
plt.show()
	



