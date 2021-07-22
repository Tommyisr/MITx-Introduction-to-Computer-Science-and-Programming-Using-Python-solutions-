# Uncomment and put your values here
# balance = 320000
# annualInterestRate = 0.2
minimum_payment = 0
monthly_interest_rate = annualInterestRate/12.0
lower_bound = balance/12
upper_bound = (balance*((1+monthly_interest_rate)**12))/12

#calculate the remaining balance after 12 months
def annual_balance(balance, payment, monthly_interest_rate):

    for i in range(1,13):

        unpaid_balance = balance - minimum_payment
        balance = unpaid_balance + monthly_interest_rate * unpaid_balance

    return balance


new_balance = balance
while new_balance!=0:
    mid_bound = (lower_bound+upper_bound)/2
    minimum_payment = mid_bound
    new_balance = balance
    new_balance = round(annual_balance(new_balance, minimum_payment, monthly_interest_rate),2)
    # print('Remaining balance:', round(new_balance, 2))
    # print('Lowest Payment: ', minimum_payment)
    if new_balance>0:
        lower_bound = mid_bound
    elif new_balance<0:
        upper_bound = mid_bound

print('Lowest Payment: ', round(minimum_payment,2))


