import numpy as NumPy

#List VS Numpy
from time import process_time

python_List = [i for i in range(10000)]

start_time = process_time()

python_List = [i + 5 for i in python_List]

end_time = process_time()

print(end_time)

