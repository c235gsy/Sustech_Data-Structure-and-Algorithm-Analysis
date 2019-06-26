import time
import numpy as np
import sys
sys.setrecursionlimit(1000000)


# 直接插入排序
def insert_sort(alist):
    start = time.time()
    for i in range(len(alist)):
        for j in range(i):
            if alist[i] < alist[j]:
                alist.insert(j, alist.pop(i))
                break
    print("直接插入排序: " + str(len(alist))+" , " + str(time.time()-start))
    return alist


# 希尔排序
def shell_sort(alist):
    start = time.time ()
    gap = len(alist)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(alist)):
            for j in range(i % gap, i, gap):
                if alist[i] < alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]
    print("希尔排序: " + str(len (alist)) + " , " + str (time.time () - start))
    return alist


# 简单选择排序
def select_sort(alist):
    start = time.time ()
    for i in range(len(alist)):
        x = i  # min index
        for j in range(i, len(alist)):
            if alist[j] < alist[x]:
                x = j
        alist[i], alist[x] = alist[x], alist[i]
    print ("简单选择排序: " + str (len (alist)) + " , " + str (time.time () - start))
    return alist


# 堆排序
def heap_sort(alist):
    start = time.time ()

    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = \
                heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, alist = alist.copy(), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        alist.insert(0, heap.pop())
        heap_adjust(0)
    print ("堆排序: " + str (len (alist)) + " , " + str (time.time () - start))
    return alist


# 冒泡排序
def bubble_sort(alist):
    start = time.time ()
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    print ("冒泡排序: " + str (len (alist)) + " , " + str (time.time () - start))
    return alist


# 快速排序
def quick_sort(alist):
    start = time.time()

    def recursive(begin, end):
        if begin > end:
            return
        left, right = begin, end
        pivot = alist[left]
        while left < right:
            while left < right and alist[right] > pivot:
                right -= 1
            while left < right and alist[left] <= pivot:
                left += 1
            alist[left], alist[right] = alist[right], alist[left]
        alist[left], alist[begin] = pivot, alist[left]
        recursive(begin, left - 1)
        recursive(right + 1, end)

    recursive(0, len(alist) - 1)
    print ("快速排序: " + str (len (alist)) + " , " + str (time.time () - start))
    return alist


# 归并排序
def merge_sort(alist):
    start = time.time ()

    def merge_arr(left_mark, right_mark):
        alist = []
        while len(left_mark) and len(right_mark):
            if left_mark[0] <= right_mark[0]:
                alist.append(left_mark.pop(0))
            elif left_mark[0] > right_mark[0]:
                alist.append(right_mark.pop(0))
        if len(left_mark) != 0:
            alist += left_mark
        elif len(right_mark) != 0:
            alist += right_mark
        return alist

    def recursive(alist):
        if len(alist) == 1:
            return alist
        mid = len(alist) // 2
        left_mark = recursive(alist[:mid])
        right_mark = recursive(alist[mid:])
        return merge_arr(left_mark, right_mark)

    print("归并排序: " + str (len (alist)) + " , " + str (time.time () - start))
    return recursive(alist)


seq = list(np.random.randint(-1000000, 1000000, size=10000))
insert_sort(seq)
shell_sort(seq)
select_sort(seq)
heap_sort(seq)
bubble_sort(seq)
quick_sort(seq)
merge_sort(seq)