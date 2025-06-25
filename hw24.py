#WA RECURSIVE FXN TO PRINT ALL ELEMENTS IN A LIST(PARAMETER = LIST,IDX)
nums= [2,3,4,5,6,7]
def print_list(list,idx=0):
    if(idx == len(list)):
        return 
    print_list(list[idx])
    return print_list(list,idx+1)    

print(nums)