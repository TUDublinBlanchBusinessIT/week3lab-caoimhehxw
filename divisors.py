#Caoimhe Walsh 
#7th of February 
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder

#define the funciton header called divisors expecting one argument
def divisors (num):
    #set up an empty list to hold your result
    myList = []
    #loop i from 1 to the number you are checking (take care not to include the number itself)
    for i in range (1, num):
        if num % i == 0: 

        #if the remainder when dividing the number by i is equal to zero
        #then i is a divisor so...
            myList.append(i)


    return myList 
        

print (divisors(20))
