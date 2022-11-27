import matplotlib.pyplot as plt
import numpy as np

def sine(t):
    return np.sin(2*np.pi*t)
def cosine(t):
    return np.cos(2*np.pi*t)
def polynomial(x,y,deg):
    curve=np.polyfit(x,y,deg)
    graph=np.poly1d(curve)
    new_x=list()
    new_y=list()
    for i in range(len(x)):
        new_x.append(x[i])
        curl=graph(x[i])
        new_y.append(curl)
    plt.plot(new_x,new_y,label="y = "+str(graph))
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.legend()
    plt.show()
def exponential(t):
    return np.exp(t)
while(True):
    choice = int(input("1.sine\n2.Cosine\n3.Polynomial\n4.Exponential\nEnter your choice:"))
    if(choice==1):
        t1 = np.arrange(0,1.57,3.14)
        plt.subplot(212)
        plt.plot(t1,sine(t1))
        plt.show()
    if(choice==3):
        n=int(input("Enter the number of plottings values: "))
        x=[]
        y=[]
        for i in range(n):
            x1=int(input("Enter the value of x coordinate for polynomial: "))
            x.append(x1)
            y1=int(input("Enter the value of y coordinate for polynomial: "))
            y.append(y1)
        degree=int(input("Enter the degree of the polynomial: "))
        polynomial(x,y,degree)
    
                         

