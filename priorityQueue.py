import copy

## Node class
class Node:
    def __init__(self, state=None, parent=None, g=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        
        self.h = 0  # h(n) for this node (Manhattan Dist/estimated future dist * w)
        self.g = g  # g(n) for this node (moves already taken)
        self.f = 0  # f(n) for this node (g(n) + h(n))
        
    def __eq__(self, other): # overload ==
        return self.state == other.state
        
    def __contains__(self, queue): # overload in keyword
        return self.state in queue

## Priority Queue; pops minimum value for A*
class PriorityQueue:
    def __init__(self): # q = PriorityQueue()
        self.queue = []
        
    def __repr__(self): # print(q)
        return ' '.join([str(i.f) for i in self.queue])
    
    def isEmpty(self): # q.isEmpty()
        # return True if length of queue is 0, otherwise False
        return len(self.queue) == 0
    
    def push(self, node): # q.push(data)
        # add data to queue; order does not matter
        self.queue.append(node)
        
    def pop(self, node):
        ind = self.queue.index(node)
        popped = self.queue.pop(ind)
        return popped
        
    def pop_min(self):
        # find minimum value
        min_index = 0;
        for i in range(len(self.queue)):
            if (self.queue[i].f < self.queue[min_index].f):
                min_index = i
        # pop minimum and return value
        min = self.queue.pop(min_index)
        return min;
