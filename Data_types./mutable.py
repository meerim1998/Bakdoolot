a = "Hello World"
print(id(a))
a = a.replace("o" , "a")
print(a)

shopping = ["Bread", "Water", "Vine", 6122022]
print(shopping[0])
print(shopping[-1])
print(shopping[2])
print(shopping[1])
print(id(shopping))
shopping.append(a)
print(id(shopping))
print(shopping)


contacts = {"Meerim":"9174963110"}
print(contacts["Meerim"])

b = {'Baha': 0, 'Meerim': 1, 'Bekzhan': 2, 'Dinara': 3}
print(b["Baha"])
print(b["Meerim"])
print(b["Bekzhan"])
print(b["Dinara"])

ix = []
for i in range(1, 1000):
    ix.append(i)
    ix.append(i+1)

print(set(ix))

