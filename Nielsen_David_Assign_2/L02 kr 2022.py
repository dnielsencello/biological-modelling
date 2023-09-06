# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:05:36 2022

@author: Keith Roper
"""

''' Loops and Conditional Statements '''

# Loops - repeat execution of a code a specified number of times
# Conditional - execute a code under specified circumstances

''' if ... elif ... else '''
'''
if (logical condition):
    Block of statements for the true condition 
elif (logical condition):
    Block of statements for the true condition 
elif (logical condition):
    Block of statements for the true condition 
else:
    Block of statements for the false condition of the previous Else If statement. 
'''
def conditionalStatements1(num):
    if num == 0:
        print('number is equal to 0')
        print(num == 0)
    else:
        print('number is not equal to 0')
        if num < 0:
            print('number is less than 0')
        elif num >0:
            print('number is greater than 0')
 
''' Comparison Operators
•	equal ( == )
•	less than ( < )
•	greater than ( > )
•	less than or equal ( <= )
•	greater than or equal ( >= )
•	not equal ( != ). 
'''

def conditionalStatements2(num):
    if num == 0:
        print('number is equal to 0')
    elif num < 0:
        print('number is less than 0')
    elif num >0:
        print('number is greater than 0')
    if num >= 0:
        print('number is greater than or equal to 0')
    if num <= 0:
        print('number is less than or equal to 0')
    if num !=0:
        print('number is not equal to 0')

def fun():
    pass


''' Two or more conditions '''

''' conjunctions between comparison operators
•	and
•	or
'''

def conditionalStatements3(num):
    if type(num) != str:
        # This if statement checks for acceptable numerical input
        if type(num) == int or type(num) == float:
            print('number is integer or floating point')
        if isinstance(num, int) or isinstance(num, float):
            print('number is integer or floating point')
        #These if statements check for acceptable integer or floating point input    
            if num == 0:
                print('number is equal to 0')  
            else:
                print('number is not equal to 0')
                if num < 0 and isinstance(num,int):
                    print('number is integer less than 0')
                elif num < 0 and isinstance(num,float):
                    print('number is floating point less than 0')
                elif num > 0 and type(num) == int:
                    print('number is integer greater than 0')
                elif num > 0 and type(num) == float:
                    print('number is floating point greater than 0')
        elif type(num) == complex:
            print('number is complex')
 # must input a string with quotations ('string') to activate else   
    else:
        print('number is not integer, floating point, or complex')

''' for Loop '''
'''
- iterates a block of code a specified number of times
- index (commonly i,j, or k) - increments each iteration of the for Loop
    can be accessed
- range() - specifies the values accessed by the index
    first number in the range is 0
        example: range(3) generates [0,1,2] and iterates i=0,1,2
    can increment values <> 1 - this is also called a 'step'
        range(initVal,termVal,increment)
'''
def loops(termval):
    for i in range(termval):
        if i == 0:
            j=1
            k=1
        print('index = '+str(i)+' in loop '+str(i))
        j=j+1
        print('j = ', j,'in loop', i)
        k+=1
        print('k = ', k,'in loop', i)
i=0; j=0; k=0;
def loopspec(init,term,inc):
    i=1
    k=1
    for j in range(init,term,inc):
        if j == 1:
            print('index = '+str(j)+' at step '+str(j))
        i=i+1
        print('i = ', i,'at step', j)
        k+=1
        print('k = ', k,'at step', j)

# Observe: k +=1 is equivalent to k=k+1
# similarly, k *= 2 is equivalent to k = k * 2
# k /= 2 is equivalent to k = k /2

import string
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
#print(alphabet_list)
def loopalpha(init,term,inc):
    for i in range(init,term,inc):
        print('Letter '+str(i)+' in alphabet is '+alphabet_list[i])

''' Combining for Loop and if statement '''

# modulo function: returns the remainder from dividing the 1st argument by the 2nd
# example: x % 2 returns 0 if x is an even number

def modexample(init,term,inc):
    for i in range(init,term,inc):
        if i % 2 == 0:
            print(str(i)+' is divisible by 2')
        elif i % 3 == 0:
            print(str(i)+' is divisible by 3')
        elif i % 5 == 0:
            print(str(i)+' is divisible by 5')
        else:
            print(str(i)+' is divisible by 1')

# value 'i' cascades through the statements until a conditional statement
# is evaluated as TRUE, at which point the code is executed, and the for Loop
# increments.  If no conditions are TRUE, the else code executes.
# the 'else' always executes if preceding condition(s) are not TRUE

''' while Loop'''

'''
executes code until a condition is met
while <insert logical condition:
    <do some action>
'''

def heater(maxtemp,step):
    if maxtemp <=20:
        temp = 0
        timeunit = 0
        while temp <= maxtemp:
            if timeunit % 1 == 0:
                print('temp at timeunit '+str(timeunit)+' is '+str(temp))
            timeunit += 1
            temp += step
    else:
        print('maxtemp '+str(maxtemp)+' is >20')
        
from Bio.Seq import Seq
NA_seq = 'Agtacactgga'.upper()
NA_seq_list  = list(NA_seq)

NA_seq_comp = NA_seq_list
NA_seq_join = ''
def compliment(NA_seq):
    NA_seq = NA_seq.upper
    print('Sequence: ' + str(NA_seq)
    for i in range(len(NA_seq_list)):
        if NA_seq_list[i] == 'A':
            NA_seq_comp[i] == 'T'
        elif NA_seq_list[i] == 'T':
            NA_seq_comp[i] == 'A'
        elif NA_seq_list[i] == 'C':
            NA_seq_comp[i] == 'G'
        elif NA_seq_list[i] == 'G':
            NA_seq_comp[i] == 'C'
    print('Compliment: ' + str(NA_seq_comp))
    
