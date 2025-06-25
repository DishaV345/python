#RRECURSIONS :when a fxn calls itself repeatedly,like loops
#              -> base case ==stoppinng condn

#recursive fxn
def show(n):
    if n == 0:
        return
    print(show)
    show(n-1)
    

show(5)    