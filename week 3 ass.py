def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after applying the discount, or the original price
    if the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get input from the user
try:
  original_price = float(input("Enter the original price of the item: "))
  discount = float(input("Enter the discount percentage: "))

  final_price = calculate_discount(original_price, discount)

  if final_price == original_price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
  else:
    print(f"The final price after a {discount}% discount is: ${final_price:.2f}")

except ValueError:
  print("Invalid input. Please enter numeric values for price and discount.")
