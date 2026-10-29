#Problem 9: Electricity Bill <a,b,c>
def electricity_bill(kwh):
    fee = 2000
    if kwh < 0:
        return None
    if kwh < 51:
        billk = kwh * 480
    if kwh < 201:
        bill = kwh * 610
    else:
        bill = kwh * 730
    total_riel = (bill + fee) * 1.1
    return round(total_riel, 2)

print (f"Test: 35kwh = {electricity_bill(35)} riels\n")

exchange_rate = 4100
for i in (0, 35, 50, 120, 200, 350):
    Usd = electricity_bill(i) / exchange_rate
    print (f"{i} kwh -> {electricity_bill(i)} riels ( ~ {Usd:.{2}f} USD)")

print ('\n-------USER INPUT-------\n')
user_in = int(input("Enter your monthly kwh: "))
riel = electricity_bill(user_in)
usd = electricity_bill(user_in) / exchange_rate
print (f"User: {user_in} -> {riel} riels ( ~ {usd:.{2}f} USD)\n")