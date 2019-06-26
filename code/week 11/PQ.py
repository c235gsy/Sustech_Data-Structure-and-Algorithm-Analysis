# 满二叉树 只有最后一层有None节点
# 完全二叉树 每一个节点都有两个节点
import random


class MinHeap(object):
    """最小堆"""
    def __init__(self):
        self.data = []  # 创建堆
        self.count = len(self.data)  # 元素数量

    def __str__(self):
        return str(self.data)

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        # 插入元素入堆
        self.data.append(item)
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, count):
        # 将插入的元素放到合适位置，保持最小堆
        while count > 1 and self.data[(count//2)-1][0] > self.data[count-1][0]:
            self.data[(count//2)-1], self.data[count-1] = self.data[count-1], self.data[(count//2)-1]
            count //= 2

    def extract_min(self):
        # 出堆
        if self.count > 0:
            ret = self.data[0]
            self.data[0], self.data[self.count-1] = self.data[self.count-1], self.data[0]
            self.data.pop()
            self.count -= 1
            self.shift_down(1)
            return ret

    def shift_down(self, count):
        # 将堆的索引位置元素向下移动到合适位置，保持最小堆
        while 2 * count <= self.count:
            # 证明有孩子
            j = 2 * count
            if j + 1 <= self.count:
                # 证明有右孩子
                if self.data[j][0] < self.data[j-1][0]:
                    j += 1
            if self.data[count-1][0] <= self.data[j-1][0]:
                # 堆的索引位置已经小于两个孩子节点，不需要交换了
                break
            self.data[count-1], self.data[j-1] = self.data[j-1], self.data[count-1]
            count = j

    def change(self, count, value):
        self.data[count-1][0] = value
        if count > 1 and self.data[(count//2)-1][0] > self.data[count-1][0]:
            self.shift_up(count)
        else:
            self.shift_down(count)


min_heap = MinHeap()
mark = 1
expect_time = 1
# time keeper
for time_keeper in range(0, 100):
    # job scheduler
    if time_keeper % 3 == 0:
        print(str(time_keeper)+":Add:\n"+str(min_heap)+"-->", end="")
        min_heap.insert([random.randint(1, 10), "work" + str(mark)])
        print(str(min_heap))
        mark += 1
    # trouble-maker
    if not min_heap.is_empty() and time_keeper % 5 == 0:
        print (str(time_keeper) + ":Change:\n" + str (min_heap) + "-->", end="")
        k = random.randint(1, min_heap.count)
        min_heap.change(k, random.randint(1, 10))
        print (str (min_heap))
    # job scheduler
    if not min_heap.is_empty() and time_keeper >= expect_time:
        print (str (time_keeper) + ":Run:\n" + str (min_heap) + "-->", end="")
        current_work = min_heap.extract_min()
        expect_time += current_work[0]
        print (str (min_heap))

