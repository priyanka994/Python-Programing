import re

def is_strong_password(password):
    # Check if the password is at least eight characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if the password has at least one digit
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[^a-zA-Z0-9\s]', password):
        return False

    # If all conditions are met, the password is considered strong
    return True

# Example usage:
password = "StrongPass123@"
if is_strong_password(password):
    print(f"The password '{password}' is strong.")
else:
    print(f"The password '{password}' is not strong.")
