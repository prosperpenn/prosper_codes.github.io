number = int(input("Enter a number: "))
limit = int(input("Enter the table limit: "))

print("\n========== MULTIPLICATION TABLE ==========")

for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

print("\n============ DIVISION TABLE =============")

for i in range(1, limit + 1):
    print(f"{number * i} ÷ {number} = {i}")
