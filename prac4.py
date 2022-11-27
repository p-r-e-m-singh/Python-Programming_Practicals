num= int(input("ENter the number to get the digits of : "))
list=[] #To store the digits 
while(num>0):
    list.append(num%10)
    num = num//10
list.reverse()
print(list)
