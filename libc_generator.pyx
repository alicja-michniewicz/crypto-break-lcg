from libc.stdlib cimport srand
from libc.stdlib cimport rand

cpdef seed(i):
    srand(i)

cpdef get_next():
    return rand()
