#CONTINUE : terminates execution in current iteration , and cont execution of the loop w next
# iteration

i = 0
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue
    print(i)    
    i += 1
