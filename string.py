#case,Whitespace,and transformation
text = "hello,world!"
print(text.upper())
print(text.strip())
print(text.replace("world","python")) #" hello, python!"
# lists and joining
word= text.strip().split(",")
print(",".join(["apple","banana"]))
#Interpolating with f-settings
name,age="Alex",55
print(f"My name is{name}and I am { age}.")

