import numpy as np
from numpy import argmax


arr = [1,4,3,2,8]
n_arr = np.array(arr)

#배열 중에서 가장 큰놈의 인덱스를 반환한다.
a = np.argmax(n_arr)
a1 = np.argmin(n_arr)

print(a)
print(a1)
