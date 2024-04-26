#!/usr/bin/python3

class pq():
	def __init__(self):
		self.queue = [None]
	def getLen(self):
		return len(self.queue) - 1
	def add(self, item):
		self.queue.append(item)
		p = self.getLen()
		q = self.queue
		while p // 2 and q[p] > q[p // 2]:
			q[p], q[p // 2] = q[p // 2], q[p]
			p //= 2
	def pull(self):
		l = self.getLen()
		if l == 0:
			return
		q = self.queue
		result = q[1]
		if l > 1:
			q[1] = q.pop()
			p = 1
			while p * 2 + 0 <= l and q[p * 2 + 0] > q[p] or p * 2 + 1 <= l and q[p * 2 + 1] > q[p]:
				if q[p * 2 + 0] > q[p]:
					print('swapping', l, p, p * 2 + 0)
					q[p], q[p * 2 + 0] = q[p * 2 + 0], q[p]
					p = p * 2 + 0
				else:
					print('swapping', l, p, p * 2 + 1)
					q[p], q[p * 2 + 1], q[p * 2 + 1], q[p]
					p = p * 2 + 1
		return result

queue = pq()
for i in (10, 20, 30, 40, 50):
	queue.add(i)
	print('added', i, queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull(), queue.queue)
print('pull', queue.pull())
