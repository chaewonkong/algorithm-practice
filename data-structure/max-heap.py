"""최대 힙

백준 11279번
URL: https://www.acmicpc.net/problem/11279
"""


# x > 0이면 배열에 삽입. x == 0 이면 배열 내 가장 큰 수 출력 및 제거

class Max_Heap(object):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        # 맨 마지막에 삽입할 원소를 임시로 추가
        self.queue.append(n)
        last_index = len(self.queue) - 1

        # 부모를 타고 올라가면서 크기를 비교
        while 0 <= last_index:
            parent_index = self.parent(last_index)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            print(0)
            return -1
        self.swap(0, last_index)
        maxv = self.queue.pop()
        self.max_heapify(0)  # root에서부터 재정렬
        print(maxv)
        return maxv

    # 임시 root 값들과 자식들을 비교해 나가며 재정렬하는 함수
    def max_heapify(self, i):
        right_index = self.rightchild(i)
        left_index = self.leftchild(i)
        max_index = i

        if left_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index

        # 만약 자신이 가장 큰 게 아니면 heapify
        if max_index != i:
            self.swap(i, max_index)
            self.max_heapify(max_index)

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index-1) // 2

    def leftchild(self, index):
        return index * 2 + 1

    def rightchild(self, index):
        return index * 2 + 2


if __name__ == "__main__":
    n = int(input())
    mh = Max_Heap()
    for _ in range(n):
        x = int(input())
        if x == 0:
            mh.delete()
        else:
            mh.insert(x)
