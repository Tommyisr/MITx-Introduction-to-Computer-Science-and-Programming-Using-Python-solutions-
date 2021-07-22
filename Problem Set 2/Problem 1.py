# Uncomment and put your values here
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

monthly_interest_rate = annualInterestRate/12.0



for i in range(1,13):
    minimum_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    balance = unpaid_balance + monthly_interest_rate * unpaid_balance
    # print('Month ' + str(round(i,2)) + ' balance is: ' + str(round(balance,2)))


print('Remaining balance:',round(balance,2))
