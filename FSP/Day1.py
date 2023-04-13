# Write a program to find the mean,median and mode of a data
from statistics import mode
import numpy

sleephours =[5,6,4,3,10,6,8,4,9,5,6,7,8,6,5,6,8,6,5,6,8,9,5,7,7]

x=numpy.mean(sleephours)
y=numpy.median(sleephours)
z=mode(sleephours)
print('The mean is :',x)
print('The median is :',y)
print('The mode is',z)

