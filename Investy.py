print("Welcome to Investy")




principal = float(input("Enter the Investment Amounts: $"))
rate = float(input("Enter the Annual interest rate (in %): ")) / 100
years = int(input("Enter the number of years: "))
future_value = principal * (1 + rate) ** years
print(f"\nAfter {years} years, your investment will grow to: ${future_value:.2f}")