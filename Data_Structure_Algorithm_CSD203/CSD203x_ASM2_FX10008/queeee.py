class Queeee:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.insert(0, data)

    def remove(self):
        if len(self.queue) >= 0:
            return self.queue.pop()
        return None

    def peek(self):
        if len(self.queue) <= 0:
            return None
        return self.queue[len(self.queue) - 1]