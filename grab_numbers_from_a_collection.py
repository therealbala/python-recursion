a=[1,2,3,4,5,[10,20,3,4,5+3j,[1,2]],'hello']
def numcheck(a,el): 
    for i in a:
        if type(i)==int:
            el.append(int(i))
        elif isinstance(i,(tuple,list,set)):
             numcheck(i,el) 
    return el 
print(numcheck(a,[]))  
