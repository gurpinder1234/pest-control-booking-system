name = input("What is your name? ")
print("Hey", name)

service = input("What kind of service are you looking for? ")

service_type = input("Understood, is it for Residential or Commercial: ").strip().lower()

if service_type == "residential":
    print("It is $250 per month")
    purchase = input("Would you like to purchase it now? ").strip().lower()
    if purchase == "yes":
        print("Great! Our team is working on it now and will contact you in 2 hours")
    else:
        print("Sorry, please begin again or call us on 647-XXX-XXXX")

elif service_type == "commercial":
    print("Currently we are covering all commercials except GTA. Is it something you are interested in?")
    purchase = input("Would you like to purchase it now? ").strip().lower()
    if purchase == "yes":
        print("Great! Our team is on it and will call you shortly!")
    else:
        print("Sorry to hear that. We will call you shortly to obtain more information")

else:
    print("Please try again and enter a valid prompt to continue!")