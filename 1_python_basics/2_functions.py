def chai_bill(cups, *addons, **discount):
  total = cups * 15
  for addon in addons:
    total += 5
  total -= (total * (discount.get("discount_percent", 0)/100))
  return total


print(chai_bill(2))                                              
print(chai_bill(3, "ginger", "masala"))                          
print(chai_bill(4, "biscuit", discount_percent=10))              
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))