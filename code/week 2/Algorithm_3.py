import sys
import numpy as np
import time
sys.setrecursionlimit(10**5)


def max_subsequence_sum(sequence, left, right):

    if left == right:
        max_sum = max(sequence[left], 0)

    else:
        center = (left+right)//2
        leftsum = max_subsequence_sum(sequence, left, center)
        rightsum = max_subsequence_sum(sequence, center+1, right)
        sum1 = 0
        lefts = 0
        for i in range(center, left-1, -1):
            lefts += sequence[i]
            if lefts > sum1:
                sum1 = lefts
        sum2 = 0
        rights = 0
        for j in range(center+1, right+1):
            rights += sequence[j]
            if rights > sum2:
                sum2 = rights
        max_sum = max(sum1+sum2, leftsum, rightsum)
    return max_sum


seq = np.random.randint(-100000,100000,size=1000)
start = time.time()
result = max_subsequence_sum(seq,0,len(seq)-1)
print (time.time() - start)

