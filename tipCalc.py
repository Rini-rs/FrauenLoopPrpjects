guests = float(input('Number of guests: '))
bill = float(input('Total bill: '))
tip = float(input('Enter the tip in %: '))

tipPercentage = tip / 100 
totalTip = bill * tipPercentage
totalBill = bill + totalTip
splittedBill = totalBill / guests
# the total amount of tip each guest needs to pay
# the amount of tip for each guest pays
print(totalBill)
print(splittedBill)