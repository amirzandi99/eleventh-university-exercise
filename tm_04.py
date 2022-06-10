LoanAmount = float(input("input loan amount --------- : "))
MinInterestRate = float(input("input minimum interest rate : "))
MaxInterestRate = float(input("input maximum interest rate : "))
# 
interestRate = [10.00, 10.00, 10.00, 10.25]
LoanAmountYear = [20, 25, 30, 20]
payment = []
monthlyPayment = []
# 
for i in range(4):
    r = (MinInterestRate * LoanAmount) / (MaxInterestRate - ((MaxInterestRate + MinInterestRate) * (-1 * LoanAmountYear[i])))
    m = r / 12
    m = float("{:.2f}".format(m))
    r = float("{:.2f}".format(r))
    monthlyPayment.append(m)
    payment.append(r)
# 
file1 = open("tm_04a.txt","w")
file1.write("_\t\t\t\t\t\tLoan Amount: ")
file1.write(str(LoanAmount))
file1.write("\n\nInterest Rate\t\tDuration(years)\t\tMonthly payment\t\tTotal payment\n")
for i in range(4):
    a = '{:<20s} {:<20s}{:<20s} {:<20s}'.format(str(interestRate[i]), str(LoanAmountYear[i]),str(monthlyPayment[i]),str(payment[i]))
    file1.write(a)
    file1.write("\n")