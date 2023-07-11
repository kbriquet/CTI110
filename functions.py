def main():
    hours = getHoursWorked()
    rate = getPayRate()
    gp = calculateGrossPay(hours, rate)
    displayValues(rate, hours, gp)
#get number of hours worked
def getHoursWorked():
    hours = float(input("Enter the employee's hours worked: "))
    return hours

#get employee pay rate

def getPayRate():
    rate = float(input("Enter the employee's pay rate: "))
    return rate
# calculate the gross pay
def calculateGrossPay(hoursWorked, payRate):
    return hoursWorked * payRate
    #return grossPay

def displayValues(rate, hours, gross):
    print(rate)
    print(hours)
    print(gross)
main()
