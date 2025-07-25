import numpy as np

A = np.array([5, 6, 8, 3, 74, 25])       #declare 1D array 

print("Array : \n", A)                   #print array 

min_value=np.min(A)                   #declare minimum value
max_value=np.max(A)                        #declare maximum value
mean = np.mean(A)                                #declare mean 
standard_deviation = np.std(A)                      #declare standard_deviation
range = max_value - min_value                    #declare range
midrange = (range) / 2                          #declare midrange 
variance = np.var(A)                         #declare variance 
sort = np.sort(A)                         #declare sort 


print("Mean : ", mean)                                                                  #print mean 
print("Standard Deviation : ", standard_deviation)                                              #print standard_deviation 
print("Minimum Value : ", min_value)                                                          #print minimum value 
print("Maximum Value : ", max_value)                                                      #print maximum value
print("Range : ", range)                                                                        #print range
print("Midrange : ", midrange)                                                                #print midrange 
print("Variance : ", variance)                                                                #print variance 
print("Sorted Array : ", sort)                                                        #print sort
