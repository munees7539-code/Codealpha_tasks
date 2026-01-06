import re

# File paths
input_file = "input.txt"
output_file = "emails.txt"

# Read the input file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression for email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(email_pattern, content)

# Write emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed successfully!")
