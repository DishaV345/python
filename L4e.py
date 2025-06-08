#sets
#> immutable, unordered(no idx)
#> can store str, boolean, int, float,tuple (immutable)
#> cant store lists,dict(mutable)
#rpeated elements stored only once
# sets r mutable,elements of set r immutable
collection={1,2,3,4}
print(type(collection))
#c2={}  ->dict type  

#how to make empty set?
c2 = set()
print(type(c2))

c3= {1,"hello",2,2,2,6,9}  #unordered

print(c3)
print(len(c3)) #len of only non repeated values/sets are stored
