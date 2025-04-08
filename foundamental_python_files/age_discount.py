# Here's the scenario:
# You are creating a program to determine ticket pricing for a movie theater, where the ticket price depends on the age of the customer. Assume the age is an integer:  

#• Children (under 12): $8
#• Adults (12-64): $12
#• Seniors (65 and over): $10  

#We'll break this down into smaller steps to make it easier.  

#Here's how we'll track your progress:
#1. Checkpoint 1: Understanding Conditional Statements (Weight = 20%).
#2. Checkpoint 2:  Applying Comparison Operators (Weight = 30%).
#3. Checkpoint 3: Constructing the Conditional Statement (Weight = 50%).  

customer_age = input('Enter you age: ')
price = 0

if customer_age < 12:
    price = 8
elif customer_age <= 64:
    price = 12
else:
    price = 10

print("Your price per ticket is:",price)
