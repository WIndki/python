class Heap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.heap)

    def push(self, value):
        self.heap.append(value)
        self.length += 1
        self._heapify_up(self.length - 1)

    def _heapify_up(self, index):
        """
        向上堆化函数，用于维护堆的性质。

        参数:
        index (int): 当前节点的索引。

        功能:
        该函数通过比较当前节点与其父节点的值，如果当前节点的值大于父节点的值，
        则交换两者的位置，并递归调用自身以继续向上堆化，直到堆的性质得到维护。
        """
        parent_index = (index - 1) // 2  # 计算父节点的索引
        if index > 0 and self.heap[index] > self.heap[parent_index]:  # 如果当前节点不是根节点且当前节点的值大于父节点的值
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  # 交换当前节点与父节点的位置
            self._heapify_up(parent_index)  # 递归调用自身以继续向上堆化
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def pop(self):
        if self.length == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap.pop()
        self.length -= 1
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        """
        向下堆化函数，用于维护堆的性质。

        参数:
        index (int): 当前节点的索引。

        功能:
        该函数通过比较当前节点与其子节点的值，如果当前节点的值小于子节点的值，
        则交换两者的位置，并递归调用自身以继续向下堆化，直到堆的性质得到维护。
        """
        largest = index  # 初始化最大值为当前节点
        left_child = 2 * index + 1  # 计算左子节点的索引
        right_child = 2 * index + 2  # 计算右子节点的索引

        # 如果左子节点存在且左子节点的值大于当前最大值，则更新最大值为左子节点
        if left_child < self.length and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        # 如果右子节点存在且右子节点的值大于当前最大值，则更新最大值为右子节点
        if right_child < self.length and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        # 如果最大值不是当前节点，则交换当前节点与最大值节点的位置，并递归调用自身以继续向下堆化
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

def main():
    heap = Heap()
    heap.push(3)
    heap.push(2)
    heap.push(1)
    heap.push(4)
    heap.push(5)
    heap.push(6)
    print(heap.pop())  # 6
    print(heap.pop())  # 5
    print(heap.pop())  # 4
    print(heap.pop())  # 3
    print(heap.pop())  # 2
    print(heap.pop())  # 1

if __name__ == '__main__':
    main()