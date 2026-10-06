shoppinglist =[ ]
shoppinglist.append("apple")
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