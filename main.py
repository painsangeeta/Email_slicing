email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
format_ = (f"Your username is {username} and domain is {domain}")
print(format_)

