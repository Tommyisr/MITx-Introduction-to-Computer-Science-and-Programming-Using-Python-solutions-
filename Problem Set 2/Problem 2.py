# Uncomment and put your values here
# balance = 3329
# annualInterestRate = 0.2
minimum_payment = 0
monthly_interest_rate = annualInterestRate/12.0

#calculate the remaining balance after 12 months
def annual_balance(balance, payment, monthly_interest_rate):

    for i in range(1,13):

        unpaid_balance = balance - minimum_payment
        balance = unpaid_balance + monthly_interest_rate * unpaid_balance

    return balance


new_balance = balance
while new_balance>0:
    new_balance = balance
    minimum_payment += 10
    new_balance = annual_balance(new_balance, minimum_payment, monthly_interest_rate)


print('Lowest Payment: ', minimum_payment)


