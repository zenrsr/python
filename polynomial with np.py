import numpy as np
numbers = [6,10,0,5]
x = (np.poly1d(numbers))
number = [10,25,1,10]
y = np.poly1d(number)
print(x+y)