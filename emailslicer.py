# Email Slicer Program

email = input("Enter your Email: ")

# index = email.index("@")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Username is {username}, domain is {domain}")

