student= {
    "NAME": "DISHA",
    "age": 18,
}
print(student)
new_dict=({"NAME" : "shaurya", "age":19, "city": "delhi"})
student.update(new_dict)
print(student)

#as duplicate keys(name, age) dont exist, new value will overwrite old value,
#and new keys(city) will be added in the tupple
