valores = [-20.0, 10.5, 0.0, 7.25, -3.5, 12.75]
total = 0

for i in valores:
    if i > 0.00:
        total = total + i
        print(i)
    else:
        continue

print(f"A soma dos positivos é: {total}")