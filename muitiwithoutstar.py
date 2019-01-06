def multiply(x,y) :
    sum = 0;
    for i in range(1,y) :
        sum +=x
    
    return sum;

def multi(x,y) :
    if x==0:
        return x
    elif y==1:
        return x
    else:
       x = x + multi(x,y-1)
       return x
    

    

print multiply(5,6);

print multi(5,7);