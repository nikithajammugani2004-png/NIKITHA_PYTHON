############# inputs we need from the user
# Total rent
# total food ordered for snaking
# electicity units spend
# charge per unit
# persons living in room / flat

############ output
# total amount you've to pay.

rent = int(input("Enter the room / flat rent:"))
food = int(input("Ënter the amount of food ordered:"))
electricity_units = int(input("Enter the total electricity units spend:"))
charge_per_unit = int(input("Enter the charge per unit:"))
persons = int(input("Enter the no.of persons living in room / flat:"))

electricity_bill = electricity_units * charge_per_unit

output = (food + rent + electricity_bill) // persons
print("Each person will pay:", output)
