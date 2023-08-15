#You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?
#Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours), and ask for the number of hours to wait. 
# Your program should output what the time will be on the clock when the alarm goes off.

Que_1 = int(input("What is the time now in hrs? "))
Que_2 = int(input("In how many hrs do you want the alarm to go off? "))
 
hours = Que_2 // 24
rem_hrs = Que_2 % 24

print("Time when alarm will go off: ",Que_1 + rem_hrs)