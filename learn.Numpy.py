import numpy as np  # Importing NumPy correctly
from time import process_time

# Creating a Python list
python_list = [i for i in range(1000000)]

# Timing the Python list operation
start_time = process_time()
python_list = [i + 5 for i in python_list]
end_time = process_time()

# Print the time taken for the Python list operation
print("Time taken for Python list operation:", end_time - start_time)

# Creating a NumPy array
np_array = np.array([i for i in range(10000)])

# Timing the NumPy array operation
start_time = process_time()
np_array += 5  # This operation is vectorized
end_time = process_time()

# Print the time taken for the NumPy array operation
print("Time taken for NumPy array operation:", end_time - start_time)
