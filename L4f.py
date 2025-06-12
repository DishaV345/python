#set methods
#set.add -> adds the value inside ()
#set.remove -> removes the () value
#collection.clear() ->empties set
#collection.pop -> removes random value (randomly)
collection = set()
print(type(collection))
collection.add(2)
collection.add(7)
collection.add("apnacollege")
collection.add((2,3,4,6))
#collection.add([3,4,5]) ->ERROR: cant store lists in sets
print(collection)

collection.remove(7)
print(collection)

collection.clear()
print(collection)

c2 = {"hello", "jennie", "python"}
print(c2.pop())