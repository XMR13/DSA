"""sementara queue adalah kebalikan dari stack
dimana urutan dari queue ini merupakan FIFO (First in First Out)
"""
from collections import deque

#membuat queue
queue = deque()

#append_terdapat dqueue O(1)
queue.append(10)
queue.append(20)
queue.append(23)
print(queue)

#remove an element from the frist O(1)
queue.popleft()

print(queue)

#check the queue(first elemen)
print(queue[0])