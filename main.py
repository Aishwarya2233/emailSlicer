email=input("enter your email: ").strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
format=(f"Your username is '{username}' and domain is '{domain_name}'")
print(format)