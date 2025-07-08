
# string[start:stop:step]
name = "python programming"
print(name[0:18:2])
print(name[::1])
print(name[::])  # python programming
print(name[:])
print(name[::-1])

# string methods
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.replace("python","scala"))
print(name.find("gra"))
print(name.find("abc"))  # if not found returns -1
print(name.isupper())
print(name.islower())
print(name.isalnum())
print(name.split(" "))
print(name.count("p"))


if name.isupper():
    print("string is upper")
    print("inside if") 
    print("still inside if")
else:
    print("string is lower")
    print("inside else")
    print("still inside else")



# range(start,stop,step)
# iterate the string
for val in range(1,10,1):
    print(val)

for val in range(10,0,-1):
    print(val)

name  = 'python'
for char in name :
    print(char)


for char in name[::-1]:
    print(char)