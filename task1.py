def check_even_odd(num):
     if num % 2 == 0:
return "even"
    else:
        return"odd"
numbers = [4,7,10,13,18,21]
even, odd = 0, 0
for num in numbers:
result = check_even_odd(num)
print(f"{num} is {result}")
if result = "Even":
    even +=1
else:
    Odd += 1
   