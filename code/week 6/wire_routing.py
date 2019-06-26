from tkinter import *


class Queue:
    # A container with a first-in-first-out (FIFO) queuing policy.
    def __init__(self):
        self.list = []

    def push(self,item):
        # Enqueue the 'item' into the queue
        self.list.insert(0, item)

    def pop(self):
        # Dequeue the earliest enqueued item still in the queue. This operation removes the item from the queue.
        return self.list.pop()

    def is_empty(self):
        # Returns true if the queue is empty
        return len(self.list) == 0


global maze, column, row, width
column = 15
row = 14
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
        [-1, -1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1, -1],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]]


def get_start_state():
    return 4, 1


def get_goal_state():
    return 5, 4


def is_goal_state(state):
    return state == (5, 4)


def get_choices(state):
    # Move order is: right, down, left, up
    choices = []
    x = state[0]
    y = state[1]
    score = state_value(state) + 1
    if y != 14 and maze[x][y+1] == 0:
        choices.append([(x, y+1), "right"])
        maze[x][y + 1] = score
    if x != 13 and maze[x+1][y] == 0:
        choices.append([(x+1, y), "down"])
        maze[x + 1][y] = score
    if y != 0 and maze[x][y-1] == 0:
        choices.append([(x, y-1), "left"])
        maze[x][y - 1] = score
    if x != 0 and maze[x-1][y] == 0:
        choices.append([(x-1, y), "up"])
        maze[x - 1][y] = score
    return choices


def state_value(state):
        return maze[state[0]][state[1]]


def wire_router():
    states_to_expand = Queue ()
    states_to_expand.push (get_start_state ())
    visited_states = []
    path_to_goal = []
    path_to_current_state = Queue ()
    current_state = states_to_expand.pop ()

    turn = 0
    flag = 1
    while flag == 1:

        if is_goal_state(current_state):
            break
        elif current_state not in visited_states:
            turn += 1
            visited_states.append(current_state)
            choices_of_move = get_choices(current_state)
            for p in range(0, len(choices_of_move)):
                choice = choices_of_move[p]
                new_position = choice[0]
                direction = choice[1]
                states_to_expand.push (new_position)
                path_to_current_state.push (path_to_goal + [direction])
        current_state = states_to_expand.pop ()
        path_to_goal = path_to_current_state.pop ()
    return path_to_goal


print(wire_router())
for line in maze:
    print(line)

