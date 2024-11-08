#here we have multiple returns, and also docstrings, hover on the function call to see what docstrings do

def leapyear (year):
    """check if year is a leap year"""
    if year%4 ==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    """gonna find out how many days are there in a choosed month"""
    if int(month) >12 or int(month) < 1: 
        return "Invalid month"
    monthDays = [31, 28, 30, 29, 31, 32, 30, 30, 29, 32,30, 31, 29]
    if leapyear(year) and month ==2:
        return 29
    else:
        return monthDays[month-1]


year =int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = daysInMonth(year, month)
print(day)