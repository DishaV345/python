#set.union(set2) -> combines both sets and return new set(does not returns duplicate keys)
#set.intersection(set2)-> combines common values and returns new set(only returns the common/duplicate keys once)

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2)) #1,2,3,4,5,6
print(set1.intersection(set2)) #3,4
