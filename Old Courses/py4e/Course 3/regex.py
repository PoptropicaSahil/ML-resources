#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

name = input("Enter file:")
if len(name) < 1 : exit()
handle = open(name)

summ = list()

#ans = 0
for line in handle :
    #line.strip()
    y =  re.findall('[0-9]+',line)
    #print(y)                       wiill print list of all numbers in the line, just that they will be strings
    #print(int(y))
    #print(sum(int(y)))
    for word in y :                 #convert the strings to integers
        summ.append(int(word))
    #ans = ans + sum()

#y = re.findall('[0-9]+',handle)    #DOES NOT WORK?!!!
#print(y)
print(sum(summ))
