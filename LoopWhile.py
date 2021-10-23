# LoopWhile


a = 0
while a < 10:
    print(a)
    a += 1

print("#" * 30)

myList = ["Mohamed", "Tamer", "Habiba", "Tamer", "Habiba", "Tamer", "Habiba"]
i = 0

while i < len(myList):
    print(myList[i])
    i += 1
# ------------------------------------------------
print("#" * 30)
# ------------------------

# EX

myFavWeb = []
maxWeb = 5

while maxWeb > 0:
    web = input("Enter Your Web : https:// ")

    myFavWeb.append(f"https://{web.strip().lower()}")

    maxWeb -= 1

    print(f"WebSite Added, {maxWeb} please Left")
    myFavWeb.sort()
    print(myFavWeb)

else:
    print("Bookmark Is Full, You Cant Add More")