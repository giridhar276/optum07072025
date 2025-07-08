# fixed arguments
def display(a,b):
    return a + b

total = display(10,20)
print(total)


# default arguments
def display(a = 0,b = 0,c = 0,d = 0):
    print(a,b,c,d)
display()
display(10)
display(10,20,30)
display(10,20,30,40)





# keyword arguments
def display(b,a,c):
    print(a,b,c)
display(b=20,c=30,a=10)



# variable length aguments
def display(*args):
    for val in args:
        print(val)

display(10,20,30,40,50,60,70,80,90,20,56,43,56,43,5,534,5,43,5,34,56,43,5,43,86,732,"unix")

