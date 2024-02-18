
balance = float(raw_input('balance: '))
annualInterestRate = float(raw_input('annualInterestRate: '))
monthlyPaymentRate = float(raw_input('monthlyPaymentRate: '))

TotalPaid = 0
MonthlyInterestRate = annualInterestRate / 12.0
PreviousBalance = balance

for mouth in range(1,13):

    MinimumMonthlyPayment = monthlyPaymentRate * PreviousBalance
    MonthlyUnpaidBalance = PreviousBalance - MinimumMonthlyPayment
    UpdatedBalanceEachMonth = MonthlyUnpaidBalance + (MonthlyInterestRate * MonthlyUnpaidBalance)                
    PreviousBalance = UpdatedBalanceEachMonth
    
    print 'Month: ' + str(mouth)
    print 'Minimum monthly payment: ' + str(round(MinimumMonthlyPayment,2))
    print 'Monthly interest rate: ' + str(round(MonthlyInterestRate * UpdatedBalanceEachMonth,2))
    print 'Remaining balance: ' + str(round(UpdatedBalanceEachMonth,2))

    TotalPaid = TotalPaid + MinimumMonthlyPayment

print 'Total paid: ' + str(round(TotalPaid,2))
print 'Remaining balance: ' + str(round(UpdatedBalanceEachMonth,2))
    
