def safe_chai_bill(cups, price_per_cup):
  try:
    cups = int(cups)
    price_per_cup = float(price_per_cup)
    if cups < 1:
      return "Cups must be at least 1"
    return cups * price_per_cup
  except ValueError as err:
    return "Please enter numbers only."

print(safe_chai_bill("3", "15"))     # normal text input from a form
print(safe_chai_bill(2, 15))          # normal numbers
print(safe_chai_bill("two", 15))      # bad input -> caught
print(safe_chai_bill(0, 15))