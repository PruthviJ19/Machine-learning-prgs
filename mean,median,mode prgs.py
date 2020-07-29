

import numpy#library function
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]#specify the numbers
x = numpy.median(speed)#median formula 
#print(x)#printing x values


import numpy#library function
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]#input values
x = numpy.mean(speed)#mean formula
print(x)#to print x values 



from scipy import stats#stats library
speed = [99,86,87,88,111,86,103,87,94,7,77,85,86]#input values
x = stats.mode(speed)# mode  formula
#print(x)