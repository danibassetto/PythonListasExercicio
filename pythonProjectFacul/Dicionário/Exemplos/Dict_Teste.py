a = {"Renata": 48, "Beatriz": 14, "Paulo": 18}
print(a)
b = a
print(b)

a["Renata"] = 50
print(a)
print(b)

c = a.copy()
print(c)

a["Renata"] = 55
print(a)
print(c)
