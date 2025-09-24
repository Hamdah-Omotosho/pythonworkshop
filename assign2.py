numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

#Instructions:
 #Write a program that calculates the sum of all the even numbers in a predefined list. The list is already given in the code. Your task is to write a loop that goes through the list, and an if statement to check each number and add it to a running sum if it is even.
#Here are some hints:
#Use a for loop to go through each number in the numbers list.
#Inside the loop, use an if statement to check if the number is even (remember a number is even if it leaves no remainder when divided by 2.  (means num % 2=0)
#Use the modulo operator % to find the remainder)
#If the number is even, add it to the total variable.
# Your code goes here!
# Loop through numbers in list to filter even numbers.

for num in numbers:
    # Check if number is even. 
    if num % 2 == 0:
        # Add even number to total.
        total += num
# Print the final total
print("The sum of the even numbers is:", total)
