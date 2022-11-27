
def factorial(n): #UDF function to get the factorial of a number
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

def sumofser(n,x): #To get the serie o/p
    i =0
    j=1
    sum = 0
    while(j<=n):
        sum += ((-1)**(j-1))*(x**i)/factorial(i)
        j += 1
        i += 2
    print(sum)

#menu
print("1.To find factorial of a number\n2.To obtain sum of the serie upto nth term\n")
choice = int(input("Enter Choice: "))
if(choice==1):
    facn = int(input("Enter the value of N to get factorial of:"));
    print(factorial(facn))


elif(choice==2):
    sern = int(input("Enter the value of n in the serie :"));
    k = sumofser(2,2)
    print(k)
