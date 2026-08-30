import requests

fromCurr = "EUR"
toCurr = "INR"
response = requests.get(f"https://api.frankfurter.app/latest?from={fromCurr}&to={toCurr}")
rate = response.json()["rates"][toCurr]
value = 100
print(f"rate: {rate}")
print(f"{value} {fromCurr} = {100 * rate} {toCurr}")