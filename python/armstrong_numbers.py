# How can you make this more scalable and reusable later?
import math

def find_armstrong_numbers(numbers):
    output=[]
    for x in numbers:
        digits = str(x)
        sum=0
        for i in digits:
            sum+=int(i)**len(digits)
        if(x==sum):
            output.append(x)
    return output