# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:26:32 2022

@author: DELL
"""

# Program to check if a string
# is palindrome or not
def reverse(Pattern):
    revcomp = []
    x = len(Pattern)
    for i in Pattern:
        x = x - 1
        revcomp.append(Pattern[x])
    return''.join(revcomp)

def compliment(Nucleotide):
    comp = []
    for i in Nucleotide:
        if i == "t":
            comp.append("a")
        if i == "a":
            comp.append("t")
        if i == "g":
            comp.append("c")
        if i== "c":
            comp.append("g")
    return ''. join(comp)

my_str = str(input("Enter a sequence: "))
#change this value for a different output
#my_str = 'albohPhoBia'
 
#make it suitable for caseless comparison
my_str = my_str.casefold()

#reverse the string
comp = compliment (my_str)
rev = reverse (my_str)
revcomp = compliment (reverse (my_str))
print("Complement:", comp)
print("Reserved:", rev) 
print("Reversed Complement:", revcomp) 

#check if the stringis equal to its reverse
if list(my_str) == list(rev):
    print(my_str, "is palindrome")
else:
    if list(my_str) == list(revcomp):
        print(my_str, "is reverse palindrome")
    else:
         print(my_str, "is not a palindrome")