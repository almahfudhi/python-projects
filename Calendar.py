#!/usr/bin/env python
# coding: utf-8

# In[1]:




print("This program  determines if an entered year is a leap year or not")

year_entered = int(input("Enter a year greater than 0: "))

if ( year_entered > 0):

   print("you entered a valid year  ") 
    
   if((year_entered % 4) != 0):
        print("BUT IT IS NOT A LEAP YEAR! ")
        
   elif ((year_entered%100) == 0):
        if(year_entered %400 == 0):
            print(" AND IT IS A LEAP YEAR!")
        else:
            print("BUT IT IS NOT A LEAP YEAR!")
   else:
       print("AND IT IS A LEAP YEAR!")
        
else:
    print("you entered invalid year!")
    


# In[2]:



import sys
import os
from subprocess import *
# valid date 
print("This program calculate the day of the week for any Julian or Gregorian calendar date")

print("")

q= int(input("Enter the day:"))
m= int(input("Enter the month: "))
y= int(input("Enter the year: "))
print("you entered ",q,"/",m,"/",y)
temp =0

if((y % 4) != 0):
    if(m == 2 and q==29):
        print("IT IS NOT A LEAP YEAR! 29 of Feb doe not exit")
        temp = 1
        

elif ((y%100) == 0):
    if(y %400 == 0):
        print("")
    else:
        if(m == 2 and q==29):
            print("IT IS NOT A LEAP YEAR! 29 of Feb doe not exit")
            temp =1
else:
   print("")
        
if(temp==0):

    if (m == 1):
        m = 13  
        y= y-1
    if (m==2):
        m=14
        y=y-1


    k= y%100       
    j= y//100


    h=( q+ int((13 * (m+1))//5) + k + int(k//4) + int(j//4) - (2*j)) %7
    h = int(h)

    #rint("h ==",h) 

    # = ((h+5)%7)+1

    #rint("d ==",d)


    print("")
    print("")

    if(h==0):
         print("and the day is Saturday")
    elif(h==1):
         print("and the day is Sunday")
    elif(h== 2):
        print("and the day is monday")
    elif(h==3):
         print("and the day is Tuesday")
    elif(h==4):
         print("and the day is Wednesday")
    elif(h==5):
         print("and the day is Thursday")
    elif(h==6):
         print("and the day is Friday")

    else:
        print("Error")


# In[3]:



# full year

print("this program prints out the calender of enetered month of a specific year. ")

#Entered_month = int(input("Input the month : "))
Entered_year = int(input("Input the year : "))
days_of_week= 7

# code below for calculation of odd days 
Extra_days =(Entered_year-1)% 400
Extra_days = ((Extra_days//100)*5 + ((Extra_days % 100) - (Extra_days % 100)//4) + ((Extra_days % 100)//4)*2)%days_of_week

#defining month of the leap year
Leap_Year =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
Normal_Year =[31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31] 
temp = 0


for x in range(12):
    Entered_month = x+1
    if Entered_year % 4 == 0: 
        for i in range(Entered_month-1): # the loops calculate the day until the choose month
            temp+= Leap_Year[i] 
    else: 
        for i in range(Entered_month-1): 
            temp+= Normal_Year[i] 
    #calculate the gaps in the matrix table
    Extra_days += temp % days_of_week
    Extra_days = Extra_days % days_of_week


    #a list to match numbers to the respective month
    month ={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
            7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'} 

    # formatting the output to the user
    print("")
    print("       ",month[Entered_month], Entered_year) 
    print('Sun', 'Mon', 'Tus', 'Wed', 'Thu', 'Fri', 'Sat') 

    # formatting the spaces 
    space_char ='' 
    space_char = space_char.rjust(2, ' ') 

    #formattimg for the months with 30 days
    if (Entered_month == 9) or (Entered_month == 4) or (Entered_month == 6) or Entered_month == 11: 
        for i in range(31 + Extra_days): 

            if i<= Extra_days: 
                print(space_char, end ='  ') 
            else: 
                print("{:02d}".format(i-Extra_days), end ='  ') 
                if (i + 1)% days_of_week == 0: 
                    print() 
    #formating for February's
    elif Entered_month == 2: 
        if (Entered_year % 4) == 0: 
            last_day = 30 
        else: 
            last_day = 29

        for i in range(last_day + Extra_days): 
            if i<= Extra_days: 
                print(space_char, end ='  ') 
            else: 
                print("{:02d}".format(i-Extra_days), end ='  ') 
                if (i + 1)% days_of_week == 0: 
                    print() 
    #formatting for the months with 31 days
    else:
        for i in range(32 + Extra_days): 

            if i<= Extra_days: 
                print(space_char, end ='  ') 
            else: 
                print("{:02d}".format(i-Extra_days), end ='  ') 
                if (i + 1)% days_of_week == 0: 
                    print() 
    print("")
    print("")


# In[ ]:




