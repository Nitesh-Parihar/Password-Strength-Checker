#Password Strength Checker

#Password Strength Checking Conditions
#1. Password shuld be at least 8 characters long
#2. Password should contain at least one uppercase letter
#3. Password should contain at least one lowercase letter
#4. Password should contain at least one digit
#5. Password should contain at least one special character
#6. Password should not contain any common passwords


import re

#Function to check the password strength
def check_password_strength(password):
    
    if len(password) < 8:
        return "Password should be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit"
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter"
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?]', password):
        return "Password should contain at least one special character"
    return "Password is strong"

user_password = input("Enter your password: ")
strength = check_password_strength(user_password)

print(strength)

def password_checker():
    while True:
        user_password = input("Enter your password (or type 'exit' to quit): ")

        if user_password.lower() == 'exit':
            print("Thank you for using the password checker!")
            print("Exiting the program...")
            break 
        strength = check_password_strength(user_password)
        print(strength)
        
# #Run the password checker tool
if __name__ == "__main__":
    password_checker()