#!/usr/bin/python3

from math import inf

class PriorityQueue():
        '''A priority queue that keeps the biggest element on top'''
        def __init__(self):
                self.queue = [None]
        def len(self):
                return len(self.queue) - 1
        def add(self, item):
                self.queue.append(item)
                k, q = self.len(), self.queue
                while k // 2 and q[k] > q[k // 2]:
                        q[k], q[k // 2] = q[k // 2], q[k]
                        k //= 2
        def pull(self):
                n, q = self.len(), self.queue
                if n == 0:
                        return
                if n == 1:
                        return q.pop()
                result = q[1]
                k, q[1] = 1, q.pop()
                n = self.len()
                while True:
                        l, r = k * 2 + 0, k * 2 + 1
                        kv, lv, rv = q[k], q[l] if l <= n else -inf, q[r] if r <= n else -inf
                        if lv > kv:
                                if rv > lv:
                                        q[r], q[k], k = q[k], q[r], r
                                else:
                                        q[l], q[k], k = q[k], q[l], l
                        elif rv > kv:
                                q[r], q[k], k = q[k], q[r], r
                        else:
                                break
                return result

queue = PriorityQueue()
for i in (10, 20, 30, 40, 50, 42, 31):
        queue.add(i)
        print('added', i, queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
print('pull -->', queue.pull(), queue.queue)
