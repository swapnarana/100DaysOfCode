print("Welcome to the tip calculator.")
bill = input("What was the total bill? Rs.")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

new_bill = float(bill)
new_tip = int(tip)
new_split = int(split)

total = new_bill + (new_bill*(new_tip/100))
result = total/new_split

#result = (new_bill/new_split)*(1 + (new_tip/100))

#final_result = round(result,2)
final_result = "{:.2f}".format(result,2)

#print(final_result)
#print("Each person should pay: " + str(final_result))

res = f"Each person should pay: Rs.{final_result}"
print(res)
