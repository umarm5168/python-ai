
''' This code take name, business type and business problem as input then generate prompt using that information using f string'''

#input() function use to take input from the user
name=input("Enter your Name: ") # we use user name so we can show name with greetings.
business_type=input("Tell your business type: ") # to understand what is business so we can use it in prompt.
business_problem=input("Biggest problem you want to solve: ") # and we use this to get information of the problem that they facing in business.
budget = int(input("What is your budget in Pakistani rupees? ")) # bydefault the input() function take value as float.
# In this we use f-string to create the prompt that show to the user
prompt=f"Welcome, {name}!\n--- Your AI Prompt ---\nSuggest 3 AI solutions for a {business_type} that struggles with {business_problem}\nBudget: {budget} PKR per month"

print(prompt)
