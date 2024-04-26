#!/usr/bin/python3

class pq():
        def __init__(self):
                self.queue = [None]
        def len(self):
                return len(self.queue) - 1
        def add(self, item):
                self.queue.append(item)
                p, q = self.len(), self.queue
                while p // 2 and q[p] > q[p // 2]:
                        q[p], q[p // 2] = q[p // 2], q[p]
                        p //= 2
        def pull(self):
                n, q = self.len(), self.queue
                if n == 0:
                        return
                if n == 1:
                        return q.pop()
                result = q[1]
                p, q[1], n = 1, q.pop(), self.len()
                while p * 2 + 0 <= n and q[p * 2 + 0] > q[p] or p * 2 + 1 <= n and q[p * 2 + 1] > q[p]:
                        if q[p * 2 + 0] > q[p]:
                                q[p], q[p * 2 + 0] = q[p * 2 + 0], q[p]
                                p = p * 2 + 0
                        else:
                                q[p], q[p * 2 + 1], q[p * 2 + 1], q[p]
                                p = p * 2 + 1
                return result

queue = pq()
for i in (10, 20, 30, 40, 50, 42, 31):
        queue.add(i)
        print('added', i, queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
