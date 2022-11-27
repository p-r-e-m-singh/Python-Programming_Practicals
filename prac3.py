#Solved the problems without UDF 
out = []
num = int(input("Enter the n value to get the factorial and nth term"))
#Fibonacci Part
num1=num
n1=0
n2=1
sum=0
while(num1>0):
    sum += n1
    n1=n2
    n2=sum
    num1 = num1-1
out.append("Fibonacci : ")
out.append(sum)
#Factorial PArt

n3=1
while(num>0):
    n3 *= num
    num = num-1
out.append("Factorial : ")
out.append(n3)

print(out)
