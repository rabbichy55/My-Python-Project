import re

email = input("Enter your e-mail: ")

def is_valid_email(email):
    # Regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if email matches the pattern
    if re.match(pattern, email):
        return "Yes! This is a valid e-mail."
    else:
        return "Sorry, your e-mail is invalid. Try again."

print(is_valid_email(email))