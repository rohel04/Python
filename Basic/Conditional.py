price = 1000000
good_credit=True
percent=''
if good_credit:
    print("You need to put down '10%' ")
    percent=10
else:
    print("You need to put down '20%' ")
    percent=20
down_payment=price-(price*(percent/100))
print(f"Your down payement is: ${down_payment}")
