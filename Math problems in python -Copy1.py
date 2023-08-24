#!/usr/bin/env python
# coding: utf-8

# In[2]:

#Day 2
#write a program where user should enter an array of numbers 
# and a number, sum of two of numbers should be equal to number A
arr = []
for i in range(5):    
    usercall = int(input("enter numberes: "))
    arr.append(usercall)
print("your array: ", arr)
num1 = int(input("enter number: "))
for i in rang(arr):
    arr.
    


# In[3]:

#Day3
#find out if the user is a girl or boy from their user
username = str(input("enter the username: "))
count = username.count(username)
if count // 2 == 0:
    print("this user is a girl")
else:
    print("this user is a boy")


# In[1]:

#Day4
#finding the volume of a cone 
import math 
def cone_vol(radius, height):
    return (1/3)* math.pi*(radius ** 2) * height 

radius = float(input("enter the radius of the cone: "))
height = float(input("enter the height of the cone: "))

volume = cone_vol(radius, height)
print(f"The volume of the cone is: {volume:.2f} cubic units")


# In[ ]:

#Day5 
#given a list of N fractions, represented of two 
#lists numerator and donominator the task is to determine the count of pairs of fractions that equals 1
from math import gcd

# Function to calculate the count of pairs equal to 1
def countPairsEqualOne(numerators, denominators):
    count = 0
    n = len(numerators)

    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the greatest common divisor (GCD)
            common_divisor = gcd(numerators[i], denominators[i])
            
            # Check if the fractions are equivalent to 1
            if (
                numerators[i] // common_divisor == denominators[j] // common_divisor and
                numerators[j] // common_divisor == denominators[i] // common_divisor
            ):
                count += 1

    return count

# Input: List of numerators and denominators
numerators = [1, 2, 3, 4, 5, 6]
denominators = [2, 4, 6, 8, 10, 12]

# Calculate the count of pairs equal to 1
result = countPairsEqualOne(numerators, denominators)

# Print the result
print(f"The count of pairs of fractions equal to 1 is: {result}")
 
#Day 6
# Chef's commute time in minutes
chef_commute_time = 30

# Input for how many minutes Chef left before he was supposed to reach
minutes_before_schedule = int(input("Enter the minutes Chef left before schedule: "))

if minutes_before_schedule == chef_commute_time:
    print("Chef will reach on time.")
elif minutes_before_schedule > chef_commute_time:
    print("Chef will reach early.")
else:
    late_minutes = chef_commute_time - minutes_before_schedule
    print("Chef will reach", late_minutes, "minutes late.")


# Day 7
#given an array arr[] containing positive elements A and B 
# are two numbers defininf a range. the taske is to 
#to check if the array contains all elements in the given 
#range 
 
def find_leaders(input_array):
    length = len(input_array)
    leader_elements = []

    max_right = input_array[length - 1]
    leader_elements.append(max_right)

    for i in range(length - 2, -1, -1):
        if input_array[i] >= max_right:
            max_right = input_array[i]
            leader_elements.append(max_right)

    return leader_elements[::-1]

# Taking input for the array of positive integers
number_list = list(map(int, input("Enter the array of positive integers (space-separated): ").split()))

leaders = find_leaders(number_list)

print("Leader elements in the array are:", leaders)


