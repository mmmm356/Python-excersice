 # # I am trying to acce four number
# number_one= int(input("Insert the first number:")) 
# number_two= int(input("Insert the second number:")) 
# number_three= int(input("Insert the third number:")) 
# number_four= int(input("Insert the fourth number:")) 
# numbers= [] # array list to include the numbers

# counter= 0
# while counter < 4:
#     nuber_input = int(input("Entery the number: "))
#     numbers.append(nuber_input)
#     counter = counter + 1

# # accept the preference of our users
# choice= input("Enter your prefered calculation:multiple, average or sum :")
# # calculated the sum of the numbers
# sum = numbers[0] + numbers[1] + numbers[2] + numbers[3] 
# # calculated the average
# average = sum / 4
# # calculated the multiplication of the numbers
# multiple= numbers[0] * numbers[1] * numbers[2] * numbers[3]
# dispiayed the calculation the user chose

# if(choice=="sum"):
#     print("The sum of the number is :", sum)
# elif(choice=="average"):
#     print("The average of the number is :", average)
# elif(choice=="multiply"):
#     print("The multiplication of the number is:", multiple)
# else:

# Array searching

def arraycreation(): 
    numbers = []
# Accept the collection from users 
    user_input = input("Enter the numbers separeted by comma:")
    input_values = user_input.split(",")
    for values in input_values:
        numbers.append(int(values.strip()))
    return numbers # it returns the array that has been created
     

# # initialize index and boolean flag

def arraysearching(number, arryName):
    index = 0
    found = False
    # while loop condition based on the boolean value found
    while index < len(arryName) and not found:
        if arryName[index] == number:
            found = True # set found to true if the target is found 
        index += 1 # move to the next index 

    return found
numbers_array = arraycreation()
print(numbers_array)
numbers_array2 = arraycreation()
print(numbers_array2)

# set the value we're looking for 
target_value = int(input("Enter the numbers to search : "))
# check if the value was found and print the result
if arraysearching(target_value,numbers_array):
    print(f"value {target_value} found in the array.")
else:
    print(f"value {target_value} not found in the array.")