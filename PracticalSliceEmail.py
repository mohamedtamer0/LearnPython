# PracticalSliceEmail

name = input("Enter Your Name: ")
email = input("Enter Your Email: ")
userName = email[:email.index("@")]
print(f"Hello {name} Your Email Is {email} And UserName Is {userName}")