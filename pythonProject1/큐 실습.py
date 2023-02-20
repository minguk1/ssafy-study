size = 10
q = [0] * size
front = rear = -1

def isFull():
    return rear == size - 1

def enqueue(item):
    global rear
    if isFull():
        print("full")
        return

    rear += 1
    q[rear] = item

def isEmpty():
    return front == rear

def dequeue():
    global front
    if isEmpty():
        print("empty")
        return
    front += 1
    return q[front]

for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end=" ")
print()