import numpy as np 
import matplotlib.pyplot as plt 

#Data setup
x = np.random.uniform(-4,4,500)
y = x + np.random.standard_normal(500)+2.5
plt.plot(x,y,'o')

#Cost function
def cost(x,y,theta):
	J = np.dot( ( np.dot(x,theta) - y ).T , ( np.dot(x,theta).T - y ).T ) / (2 * len(y))
	return J

#Variable initialization
alpha = 0.1
theta = np.array([[0,0]]).T
X = np.c_[np.ones(500),x]
Y = np.c_[y]
X_1 = np.c_[x].T

#iteration for gradient descent
for i in range(100):
	a=np.sum(theta[0]-alpha * (1/len(Y)) * np.sum((np.dot(X,theta)- Y)))
	b=np.sum(theta[1]-alpha * (1/len(Y)) * np.sum(np.dot(X_1,(np.dot(X,theta)-Y))))
	theta = np.array([[a],[b]])
	print(x[1],y[1],a+b*x[1],np.sum(cost(X,Y,theta)))
	plt.plot(x,a+b*x)
