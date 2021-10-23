age = input("Please Write Your Age: ").strip()

unit = input("Please Choose Time Unit: Months, Weeks, Days: ").strip().lower()

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == "months" or unit == "m":
    print("You Choosed The Unit Month")
    print(f"You Lived For {months:,} Months.")

elif unit == "weeks" or unit == "w":
    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks.")

elif unit == "days" or unit == "d":
    print("You Choosed The Unit days")
    print(f"You Lived For {days:,} days.")