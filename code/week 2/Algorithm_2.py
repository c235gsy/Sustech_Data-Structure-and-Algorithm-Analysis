import numpy as np
import time


def max_subsequence_sum(sequence):

    max_sum = 0
    for i in range (0, len (sequence)):
        this_sum = 0
        for j in range (i, len (sequence)):
            this_sum += sequence[j]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum


seq = np.random.randint(-100000,100000,size=10)
start = time.time ()
result = max_subsequence_sum(seq)
print (time.time()-start)

