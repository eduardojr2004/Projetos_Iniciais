lista = [123, "casa", ["abc", "123"], "correio", 1515]

for i in lista:
    if not isinstance(i, int):
        continue
    else:
        print(i)