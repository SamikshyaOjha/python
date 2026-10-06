shoppinglist =[ ]
shoppinglist.append(input{"enter your 1st item"})
shoppinglist.append("banana")
shoppinglist.append("orange")
shoppinglist.append("guava")
print(shoppinglist)
shoppinglist.remove("orange")
print(shoppinglist)
if "banana" in shoppinglist:
    print("it is")
length = len(shoppinglist)
for n in shoppinglist:
    print(n)