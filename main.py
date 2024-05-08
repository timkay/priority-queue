#!/usr/bin/python3

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
                        kv = q[k]
                        lv = q[l] if l <= n else -math.inf
                        rv = q[r] if r <= n else -math.inf
                        if lv > kv:
                                # left > parent
                                if rv > lv:
                                        # right > both
                                        # parent <-> right
                                        q[k], q[r] = q[r], q[k]
                                        k = r
                                else:
                                        # left <-> parent
                                        q[l], q[k] = q[k], q[l]
                                        k = l
                        elif rv > kv:
                                # right <-> parent
                                q[r], q[k] = q[k], q[r]
                                k = r
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
