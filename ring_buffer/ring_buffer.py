from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = Queue()
        """ don't understand why/how this list is getting restarted each time
            a method is called but not .buffer"""
        self.list1 = []

    def append(self, item):
        if len(self.list1) == self.capacity:
            value = self.queue.dequeue()
            index = self.list1.index(value)
            self.list1.remove(value)
            self.list1.insert(index, item)
            self.queue.enqueue(item)
        else:
            self.list1.append(item)
            self.queue.enqueue(item)

    def get(self):
        return self.list1