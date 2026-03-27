import heapq
import random

class Node:
    def __init__(self, state, action=None, parent=None):
        self.state = state
        self.action = action
        self.parent = parent
        self.family_tree =self.get_family_tree()

    def get_family_tree(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

class StackSpace:
    def __init__(self):
        self.frontier=[]
    def add(self,node):
        self.frontier.append(node)

    def is_empty(self):
        return len(self.frontier) == 0

    def remove(self):
      if self.is_empty():
          raise Exception("Stack space is empty")
      return self.frontier.pop()

    def contains_state(self, state):
        for node in self.frontier:
            if node.state == state:
                return True
        return False


class QueueSpace:
    def __init__(self):
        self.frontier=[]
    def add(self,node):
        self.frontier.append(node)
    def is_empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.is_empty():
            raise Exception("Queue space is empty")
        return self.frontier.pop(0)
    def contains_state(self, state):
        for node in self.frontier:
            if node.state == state:
                return True
        return False


class PriorityQueueSpace:
    def __init__(self):
        self.frontier=[]
        self.counter=0
    def add(self,node,priority):
        heapq.heappush(self.frontier,(priority,self.counter,node))
        self.counter+=1

    def is_empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        return heapq.heappop(self.frontier)[2]

    def contains_state(self, state):
       for _,_, node in self.frontier:
           if node.state == state:
               return True
       return False
def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    x, y = 0, 0
    maze[x][y] = 0
    while (x, y) != (size-1, size-1):
        if x == size-1:
            y += 1
        elif y == size-1:
            x += 1
        else:
            if random.random() < 0.5:
                x += 1              #tu random aris 0.5ze naklebi chavidet ertit dabla
            else:
                y += 1 #tuarada gavidet ertit marjvniv
        maze[x][y] = 0             #movnishnot current state rogorc gza da ara kedeli.

    for _ in range(size*size//3):
        i, j = random.randint(0, size-1), random.randint(0, size-1)  #gavxsnat ufro meti gza rata maze ikos ufro unpredictable
        maze[i][j] = 0
    return maze

def print_maze(maze, path=None):
    maze_copy = [row[:] for row in maze]
    if path:
        for x, y in path:
            maze_copy[x][y] = '*'
    for row in maze_copy:
        line = ''
        for cell in row:
            if cell == 1:
                line += '#'  # wall
            elif cell == 0:
                line += '.'  # open space
            else:
                line += '*' # path
        print(line)

def bfs(maze):
    size = len(maze)
    start = (0,0)
    goal = (size-1, size-1)
    frontier = QueueSpace()
    frontier.add(Node(start))
    explored = set()

    while not frontier.is_empty():
        node = frontier.remove()
        x, y = node.state
        if node.state == goal:
            return node.get_family_tree()  # path from start to goal
        explored.add(node.state)

        # explore neighbors
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # up, down, left, right
            nx, ny = x+dx, y+dy
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == 0:
                if (nx, ny) not in explored and not frontier.contains_state((nx, ny)):
                    frontier.add(Node((nx, ny), parent=node))
    return None


maze_size = 8
let_maze = generate_maze(maze_size)
print_maze(let_maze)
let_path = bfs(let_maze)

print("*******************AFTER EXPLORING************************")
print_maze(let_maze, let_path)
