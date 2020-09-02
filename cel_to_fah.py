import matplotlib.pyplot as plt 
import matplotlib.style 
import numpy as np 

plt.style.use("fivethirtyeight")

def conv(X):
	'''convert celsius to fahrenheit'''
	return X*(9/5) + 32

r1 , r2 = int(input("Enter lower limit\t")) , int(input("Enter upper limit\t"))
celsius = np.linspace(r1,r2,num=50)
fahrenheit = conv(celsius)

ax = plt.gca()
plt.plot(celsius, fahrenheit , linestyle="-" , color = 'b' , linewidth=3,  label = "Celsius and Fahrenheit")
plt.plot(ax.get_xlim(), [0,0] , linestyle='--' , color='k', linewidth=2)
plt.plot([0,0],ax.get_ylim(), linestyle='--' , color = 'k', linewidth=2)

plt.xlabel("Celsius")
plt.ylabel("Fahrenheit")
plt.title("Fahrenheit wrt Celsius")
plt.legend()

plt.show()