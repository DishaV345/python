
def val(b,a=2):
    val = b
    if b%a ==0:
        print("EVEN")
    else:
        print("ODD")
        print(val)
        return val
    
b= int(input("enter num: "))    
    
val(b)