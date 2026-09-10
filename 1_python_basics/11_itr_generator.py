numbers = [i for i in range(10)]
itr = iter(numbers)
rev_itr = reversed(numbers)

# while (n := next(itr, None)) is not None:
#   print(f"{n}")

print(f"{', '.join(str(i) for i in rev_itr)}")

# Generator (yield)
def fib(n):
  a, b, i = 0, 1, 0
  while i < n:
    yield a
    a, b, i = b, a+b, i+1

print(f"Fib Series: {', '.join(str(i) for i in fib(10))}")

print([i*i for i in range(6)])

set = {1,2,3,3} # set = Set(), unordered, unique
dict = {'a': 11}

print(f"set: {type(set)}, dict: {type(dict)}")

keys = ["name", "age", "marks"]
values = ["Nikhil", 30, 100]
print({k:v for k, v in zip(keys, values)})

