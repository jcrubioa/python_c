import ctypes
import time

lib_path = r'./heavy_task.dll' # For Windows
# lib_path = r'./heavy_task.so' # For Linux
handle = ctypes.CDLL(lib_path) # Load library
handle.calculate.argtypes = ctypes.c_int,
handle.calculate.restype = ctypes.c_longlong


def calculate_c(n):
    return handle.calculate(n)


start = time.time()
print("Result: ", calculate_c(100000000))
end = time.time()
print("C Extension Time: {}".format(end-start))
