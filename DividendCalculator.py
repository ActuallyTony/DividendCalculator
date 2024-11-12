actualPayPerMonth = 0
targetPayPerMonth = 4000

monthsInvesting = 0
investmentPerMonth = 100

startingAmount = 0
totalInvested = startingAmount

payoutPeriodInMonths = 3 # 3 means quarterly payout | 1 means monthly
dividendAnnualAverage = .05 # Average annual dividend payout

while actualPayPerMonth < targetPayPerMonth:
    monthsInvesting += 1
    totalInvested += investmentPerMonth

    # Checks if it's a payout period and then automatically reinvests that money
    if monthsInvesting % payoutPeriodInMonths == 0:
        totalInvested += totalInvested * (dividendAnnualAverage / (12 / payoutPeriodInMonths))

    actualPayPerMonth = totalInvested * (dividendAnnualAverage / 12)
    
print("Years: ", (monthsInvesting // 12))
print("Months: ", (monthsInvesting % 12))
print("Personal Invested: ", ((monthsInvesting * investmentPerMonth) + startingAmount))
print("Total Invested: ", totalInvested)

input()