s = input("Enter the string :")
op= dict()
for   i in s:
    op[i] =0;
          
for   i in s:
    op[i] += 1;
            
print("Frequency Dictionary: ",op)
