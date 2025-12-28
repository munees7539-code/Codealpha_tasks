import re

# Open and read input file
file = open("input.txt", "r")
text = file.read()
file.close()

# Find email addresses
emails = re.findall(r'\S+@\S+', text)

# Save emails to output file
output = open("emails.txt", "w")
for email in emails:
    output.write(email + "\n")
output.close()

print("Email addresses extracted and saved to emails.txt")
