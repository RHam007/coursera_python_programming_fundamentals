def calculate_discount(price, discount_percentage):
  """
  This is a provided function for debugging purposes.

  The function contained an operation error within the discounted_price formula:
    discounted_price = price + discount_amount >>> Changed to: >>> discounted_price = price - discount_amount

  There is an opportunity to explore advanced debugging and try-except logic to address potential common user based operational errors
  not explored in this example.
  """
  discount_amount = price * (discount_percentage / 100)
  discounted_price = price - discount_amount
  return discounted_price

price = 50

discount_percentage = 20

discounted_price = calculate_discount(price, discount_percentage)

print(discounted_price)
#calculate_discount(50,20)