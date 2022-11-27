def checknum(l:list):
    for i in l:
        if(type(i)!=int):
            return False
        
    return True

def oddvalno(l):
    if(checknum(l)):
        cnt=0
        for i in l:
            if(i%2!=0):
                cnt += 1

        return cnt   
    else:
        return -1

def largeststr(l):
    if(~checknum(l)):
        return max(l)

def displayrev(l):
    for i in range(len(l)-1,-1,-1):
        print(l[i]," ")

def linearsearch(l:list,ele):

    for i in range(0,len(l),1):
        if(ele==l[i]):
            return i
        else:
            return "Not Found"

def removespecified(l:list,ele):
    l.remove(ele)
    
def sortindesc(l:list):
    for i in range(1,len(l),1) :
        key = l[i]
        j = i-1
        while(j>=0 and key<l[j]):
            l[j+1]=l[j]
            j -= 1
        l[j+1]=key
    l.reverse()
    print(l)

def findcommon(l1,l2):
    opl = []
    for i in l1:
        for j in l2:
            if(i==j):
                opl.append(i)
    return opl