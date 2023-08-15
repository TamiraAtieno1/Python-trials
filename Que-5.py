#Write a Python program that assigns the principal amount of $10000 to variable P, 
# assign to n the value 12, and assign to r the interest rate of 8%. 
# Then have the program prompt the user for the number of years t that the money will be compounded for. 
# Calculate and print the final amount after t years.
# A = P (1 + r/n)nt

P = 10000
n = 12
r = 0.08
response = input("What is the number of years? ")
t = float(response)
A = 10000 * (1 + 0.08/12)**(12*t)
print("The final amount is ", A)