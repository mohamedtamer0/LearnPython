# Your Age

age = int(input("What\'s Your Age ? ").strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('You Lived For:')
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")