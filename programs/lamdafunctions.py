# traditional way 
def display(a,b):
    return a + b

total = display(10,20)
print(total)


#lambda function- is the replacement of single liner functions
# more optimized way of writing the block
#syntax
#functioname = lambda variables : expresssion

display = lambda a,b : a + b
total = display(10,20)
print(total)


## length of the string
length = lambda s: len(s)
print(length("hello"))



# Convert string to lowercase
to_lower = lambda s: s.lower()
print(to_lower("HeLLo"))


# Check if "data" in string
contains_data = lambda s: "data" in s
print(contains_data("data science")) 