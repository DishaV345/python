#dict   -> mutable, unordered(no indexing)*  , no duplicate keys(replicate key not possible)

dict = {
    "key"  : "value",
    "name" : "disha ",
    "age" : 18,
    "learning" : "python",
}
print(dict)

#to add more in dict, 
dict["surname"] = "varun"
print(dict)

#to change dict(mutate),
dict["age"] = 19
print(dict)