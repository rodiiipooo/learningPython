import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import pandas_datareader.data as reader
import statsmodels.api as sm
import seaborn as sb

space = '**************************'
columnNames = ["year", "General Manager(Total, millions)", "General Manager(Legal Fees, millions)", "Legal_Fees_as_%Total", "All_else_as_%Total"]

data = [[2015, 1.47, 0.96],
         [2016, 1.54, 1.03],
         [2017, 2.11, 1.53],
         [2018, 1.91, 1.30],
         [2019, 2.18, 1.60],
         [2020, 2.02, 1.40],
         [2021, 2.19, 1.60]]
i = 0
while i < len(data):
    data[i].append(round(data[i][2]/data[i][1], 2))
    data[i].append(round(1 - data[i][3], 2))
    i += 1
df = pd.DataFrame(data, columns=columnNames)

print(df)
plt.plot(df['year'], df['Legal_Fees_as_%Total'], color="green", linewidth=2, label='Legal Fees, %')
plt.plot(df['year'], df["All_else_as_%Total"], color="red", linestyle="--", label="All Other Expenses, %")

plt.bar(df['year'], df['Legal_Fees_as_%Total'], color="green",  bottom=df["All_else_as_%Total"], alpha=0.1)
plt.bar(df['year'], df["All_else_as_%Total"], color="red", alpha=0.1)
plt.grid()
plt.legend()
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title("Legal Fees vs All Other General Administration Expenses (2015-2021)")
plt.show()

