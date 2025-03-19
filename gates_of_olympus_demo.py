import random

print("Gates of Olympus Demo - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Божественный Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Попробуй демо и крути на деньги в топ-казино!")
