i = 1
totalyes = 0
totalno = 0

while i <= 3:
    while True:
        sugar = input("Did you consume sugar today, Yes/No: ")

        if sugar.lower() == "yes":
            print("Got it, Added!, Not good though")
            totalyes += 1
            percentage += 1
            break

        elif sugar.lower() == "no":
            print("Good, Added")
            totalno += 1
            break

        else:
            print("Please enter yes or no")

    i += 1

print("Total days you consumed sugar is:", totalyes)
print("Total days you have not consumed sugar is:", totalno)
print("Out of 3 days", totalno, "days were guilt free!")
percentage = (totalyes / 3) * 100
print("Total sugar consumption percentage is:", percentage, "%")