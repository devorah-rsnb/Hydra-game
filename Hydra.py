def Hydra(h, n): #n is an integer, h is a string representing the hydra
    i = 0 #iterator
    while (h[i]=='('):
        i+=1
    #print(i)
    if i<=1:
        return "dead"        
    if i<=2: #this is if the first empty set is a child of the entire set
        return h[0:i-1]+h[i+1:]
    else: 
        without = h[0:i-1]+h[i+1:]
        before = h[0:i-2] #part of the string before the part to copy
        after = without[i-2:]
        tocopy = "("
        count = 1
        j = i-1
        while (count!=0):
            if (without[j]=='('):
                count+=1
            else:
                count-=1
            tocopy+=without[j]
            j+=1
        answer = before + tocopy*(n-1)+after
        return answer

def LifeCycle(h):
    i = 0
    while h!="dead":
        h = Hydra(h, i)
        print(h)
        i+=1
    return 

a = "(()(((()))))"      
LifeCycle(a)
