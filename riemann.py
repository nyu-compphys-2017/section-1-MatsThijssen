# This is a python file! The '#' character indicates that the following line is a comment.
import numpy as np
# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print("hello world!")
    print(name)
    return
    
def hey(x):
	return x**2

#Implement the Riemann Sum approximation for integrals
def Riemann(func, n, a, b):
	width=(b-a)/n
	total=0
	for i in np.arange(a+width,b+width,width):
		total+=func(i)*width
	return total
print(Riemann(hey,5,1,6))	
