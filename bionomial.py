#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import random
from scipy.stats import binom 
import matplotlib.pyplot as plt 

bag=[0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

list=[]*1000  
result=[]
k=0
sum= 0 

#loop to iterate for 10000 times
while ( k <10000):
    #loop to iterate for 100 times
    for x in range(100):
        
        Random_number = random.randint(0, 9)
       # print(Random_number)
        if(bag[Random_number] == 1):
            list.append([x+1,1])
        elif(bag[Random_number] == 0):
            list.append([x+1,0])
        else:
            print("random num is :",bag[Random_number])
            
        #adding the sum of each iteration into result[]
        for y in range(len(list)): 
            sum= sum + list[y][1]
            #print("sum = ",sum)  
        list.clear()
    result.append(sum)
    sum=0
    k=k+1

    
#print(result)    

# display the digram
plt.hist(result, bins=10)

plt.title('Histogram')
plt.xlabel('# of draws per trail')
plt.ylabel('# of trails')

plt.show()

