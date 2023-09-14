def usd_to_local_currency(usd_amount, exchange_rate):
    local_currency_amount = usd_amount * exchange_rate
    return local_currency_amount

# Get the user's input for the amount in USD
usd_amount = float(input("Enter the amount in USD: "))

# Replace this with the actual exchange rate to your local currency
exchange_rate = 146.80  # 1 USD = 1.23 Local Currency

# Call the function to convert USD to your local currency
local_currency_amount = usd_to_local_currency(usd_amount, exchange_rate)

# Display the result
print(f"{usd_amount} USD is equal to {local_currency_amount} Local Currency")
