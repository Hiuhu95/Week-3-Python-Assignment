# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount and apply it to the price
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if no discount is applied
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == price:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
else:
    print(f"Final price after applying a {discount_percent}% discount: ${final_price:.2f}")
