
def summary(z):

    print(z)
    print(len(z))

titles = ["day", "balance", "'%'earnings", "'$'earnings"]

percent_earn = .15

days = 365
dayNum = []


a = 1
while a <= days:
    dayNum.append(a)
    a += 1

initialBalance = 300
balances = [initialBalance]
b = 0
while b < days-1:
    nextBal = balances[b]+(balances[b]*percent_earn)
    balances.append(nextBal)
    b += 1

dollar_earnings = []
c = 1
while c <= 365:
    nextDollarEarn = (balances[c]-balances[c-1])
    dollar_earnings.append(nextDollarEarn)
    c += 1

percent_earnings = []
d = 0
while d != 365:
    percent_earnings.append(dollar_earnings[d] / balances[d])
    d += 1
percent_earnings = []


summary(balances)