class Queue:
    def __init__(self, maxsize):
        self.__max_size = maxsize
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def getMaxSize(self):
        return self.__max_size

    def isFull(self):
        return self.__rear == self.__max_size

    def isEmpty(self):
        if self.__rear == -1 or self.__front == self.__max_size:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            print('Queue is full')
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty.')
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        if not self.isEmpty():
            for i in range(self.__front, (self.__rear + 1)):
                print(self.__elements[i])
        else:
            print('Empty queue.')

    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append(str(self.__elements[index]))
            index += 1
        msg = ' '.join(msg)
        msg = f'Queue data (from front to rear) : {msg}'
        return msg


if __name__ == '__main__':
    queue = Queue(5)
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')
    queue.enqueue('E')
    print(queue)
    print('Dequeued: ', queue.dequeue())
    print('Dequeued: ', queue.dequeue())
    print('Dequeued: ', queue.dequeue())
    print('Dequeued: ', queue.dequeue())
    print('Dequeued: ', queue.dequeue())
    print('Dequeued: ', queue.dequeue())
    queue.display()