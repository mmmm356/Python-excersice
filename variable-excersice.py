# I am trying to acce four number
number_one= int(input("Insert the first number:")) 
number_two= int(input("Insert the second number:")) 
number_three= int(input("Insert the third number:")) 
number_four= int(input("Insert the fourth number:")) 

choice= input("Enter your prefered calculation: average or sum :") 

# calculate the average
average = (number_one+number_two+number_three+number_four) / 4
# calculate the sum
sum=(number_one+number_two+number_three+number_four)

# calculate the multiplication
multiple=(number_one*number_two*number_three*number_four)

# display the result based on the condition/ choice
if(choice=="average"):
    print("The average of the number is :", average)
elif(choice=="sum"):
    print("The sum of the number is :", sum)
elif(choice=="multiply"):
    print("The multiplication of the number is:", multiple)
else:
    print(average,sum,multiple)

      


