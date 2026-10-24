
'''This code is used so the buiness owner can generate prompts for Marketing,Customer Service,Growth.This code take input from the user and generate three prompts.'''
#Taking input from users for the prompt 
business_name  = input("What is your business name? ") 
business_type  = input("Tell what type of business you are doing? ")
city           = input("City Name? ")
main_customers = input("Main customers? e.g students,families, office? ")
monthly_budget = int(input("Your budget monthly budget? ")) # i used int() function so it convert string value to integer.

#Showing the output so user can see.
print(f"Business Name: {business_name}\nBusiness Type: {business_type}\nCity: {city}\nMain Customers: {main_customers}\nMonthly Budget PKR: {monthly_budget}\n\n") # I used f-string insteading of typing print() function again and again.

print((f"===========================\n AI Prompt Kit for {business_name} \n===========================\n")) # i used this so business name on the top of the prompt
print(f"[1] Prompt for Marketing\nWrite a short Instagram post for {business_name}, a {business_type} in {city}.\nTarget {main_customers}. Friendly tone, 1 call to action.\n")
print(f'''[2] Prompt for Customer Service\nYou are the manager of {business_name}. Write a polite reply to a customer
whose order arrived late. Apologise and offer a small discount.\n''')#i used tripe quote to print multiple line.
print(f'''[3] Prompt for Growth\nSuggest 3 low-cost AI tools a {business_type} in {city} can use
to attract {main_customers} with a budget of {monthly_budget} PKR per month.''')
