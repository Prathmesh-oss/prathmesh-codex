import re

# Function to check password strength
def check_password_strength(password):
    # Conditions
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password) is not None
    lowercase = re.search(r"[a-z]", password) is not None
    digit = re.search(r"\d", password) is not None
    special = re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is not None

    # Count satisfied conditions
    count = sum([length, uppercase, lowercase, digit, special])

    # Decide strength
    if count == 5:
        return "Strong Password"
    elif 3 <= count < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Main program
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)
