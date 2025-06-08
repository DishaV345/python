#nested dict  -> dict inside dict/(if inside if)
student = {
    "name" : "disha",
    "subjects" : {
        "phys": 89,
        "chem": 75,
        "bio": 97,
    },
    "age" : 18,
}
print(student)


#if only want to print subjects
print(student["subjects"])

#if only want to print one subejct marks,
print(student["subjects"]["bio"])


