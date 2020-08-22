def odd_even(*lst):
    odd=even=0
    for i in lst:
        if(i%2==0):
            even+=1
        else: odd+=1
    return odd,even

nodd,neven=odd_even(2,9,11,46,789,944,233)
print("Even : {} and Odd : {}".format(neven,nodd))