
grossprofit = int(input("Enter Gross Profit: "))

netprofit = int(input("Enter Net Profit: "))

sales = int(input("Input Sales: "))


gpm = grossprofit/sales * 100
print("Gross Profit Margin is", gpm, "%")


npm = netprofit/sales * 100
print("Net Profit Margin is", npm, "%")