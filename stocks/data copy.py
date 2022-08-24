
from math import *
from numpy import *

def summary(x):

    print(x)
    print(len(x))

titles = ["day", "balance", "'%'earnings", "'$'earnings"]
percent_earn, days, initialBalance = .10, 365, 300
dollar_earnings, percent_earnings, dayNum, balances = [0], [0], [], [initialBalance]
overview = 

c1 = 1
while c1 <= days:
    dayNum.append(c1)
    c1 += 1


c2 = 0
while c2 < days-1:
    balances.append(balances[c2]+(balances[c2]*percent_earn))
    c2 += 1

c3 = 1
while c3 < days:
    percent_earnings.append(round(((balances[c3]/balances[c3-1])-1),2))
    c3 += 1

c4 = 1
while c4 < days:
    dollar_earnings.append(balances[c4]-balances[c4-1])
    c4 += 1


