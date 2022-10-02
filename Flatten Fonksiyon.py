l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

newList=[]

def flatten(n):

    for k in n:
        if isinstance(k,list):
            flatten(k)
        else:
            newList.append(k)

flatten(l)
print(newList)
