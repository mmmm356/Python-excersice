# create a function that computes the factorial of a number 
def factorialofnumbers(number):
    if(number == 0): #
        return 1
    else: # calculate the factorial of the number by calling the function
        return number * factorialofnumbers(number- 1)
    
number_one = int(input("Enter the number:"))

result = factorialofnumbers(number_one)

print("the factorial of", number_one, "is:", result)


