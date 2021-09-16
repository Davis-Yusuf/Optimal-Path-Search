from collections import defaultdict
import numpy as np


file = open('input.txt', 'r')

method = file.readline().strip()
if method == 'A*':
    print("A*")
elif method == 'BFS':
    print("BFS")
elif method == 'UCS':
    print("UCS")

dimensions = file.readline().split()
size_x, size_y, size_z = [int(i) for i in dimensions]
print(size_x, size_y, size_z)

entrance = file.readline().split()
entrance_x, entrance_y, entrance_z = [int(i) for i in entrance]
print(entrance_x, entrance_y, entrance_z)

exit_grid = file.readline().split()
exit_x, exit_y, exit_z = [int(i) for i in exit_grid]
print(exit_x, exit_y, exit_z)

grid_size = int(file.readline())
print(grid_size)

next_lines = file.readlines()
line_list = [i.split() for i in next_lines]


class BFS:

    def __init__(self, cost):
        self.grid = defaultdict(list)  # Creating the adjacency list
        self.cost = cost

    def add(self, a, b):
        self.grid[a].append(b)  # Adding edges

    def bfs(self, start, end):
        bfs_queue = []
        bfs_path = []
        discovered = [False for i in range(self.grid.__len__())]  # Setting all elements of the set discovered to false
        discovered[start] = True
        bfs_queue.append(start)

        while len(bfs_queue) > 0:  # While the queue is not empty, dequeue the first element S, then
            v = bfs_queue.pop(0)  # check the adjacent points, if it is not discovered, set it to true and add it
            bfs_path.append(v)  # to the queue.
            print(v)

            for j in self.grid[v]:
                if not discovered[j]:
                    discovered[j] = True
                    bfs_queue.append(j)

        return print(self)


#
#
# def ucs(self, b):
#     return print(self + b)
#
#
# def a_star(self, b):
#     return print(self + b)


# g = BFS()

for line in line_list:
    arr = np.array([int(line[i]) for i in range(3)])
    actions = np.array([int(line[i]) for i in range(3, len(line))])
    print(arr)
    print(actions)

    # for i in range(3, len(line)):
    #     actions.append(int(line[i]))
file.close()
