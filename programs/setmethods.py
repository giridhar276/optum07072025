
aset = {10,10,10,10,20,20,20,30,30}
print(aset)

bset = {30,30,30,40,40,40,50}
print(bset)


print("Union :", aset.union(bset))
print("Intersection :", aset.intersection(bset))
print("differerence :", aset.difference(bset))

aset.add(10)
print(aset)
aset.add(40)
print(aset)