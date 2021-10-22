uName = "Tamer"
cName = "Kotlin"
cPrice = 100
cDiscount = 5
uCountry = "KSA"

if uCountry == "Egypt" or uCountry == "Kuwait":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is : ${cPrice - 50}")


elif uCountry == "KSA":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is : ${cPrice - 10}")


else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is : ${cPrice - 5}")
