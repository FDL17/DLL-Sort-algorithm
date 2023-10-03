from ctypes import *

def sort_list(input_list):
    mydll = CDLL("./hasil/mys-sort.dll")
    mydll.run.argtypes = POINTER(c_double), c_int
    mydll.run.restype = None
    my_list = (c_double * len(input_list))(*input_list)
    length = len(my_list)
    mydll.run(my_list, length)
    return [my_list[i] for i in range(length)]

input_list = [7,12,1,2,9.99,9.89,2,12,3,2]
sorted_list = sort_list(input_list)
for item in sorted_list:
    print(item)
