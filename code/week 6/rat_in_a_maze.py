

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


global maze
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


def get_choices(stage):
    # Move order is: right, down, left, up
    choices = []
    x = stage[0]
    y = stage[1]
    if y != 14 and maze[x][y+1] == 0:
        choices.append([(x, y+1), "right"])
    if x != 13 and maze[x+1][y] == 0:
        choices.append([(x+1, y), "down"])
    if y != 0 and maze[x][y-1] == 0:
        choices.append([(x, y-1), "left"])
    if x != 0 and maze[x-1][y] == 0:
        choices.append([(x-1, y), "up"])
    return choices


def get_start_stage():
    return 0, 0


def get_goal_stage():
    return 13, 14


def is_goal_stage(stage):
    return stage == (13, 14)


def breadth_first_search():
    states_to_expand = Queue ()
    states_to_expand.push (get_start_stage())
    visited_states = []
    path_to_goal = []
    path_to_current_state = Queue ()
    current_state = states_to_expand.pop ()

    flag = 1
    while flag == 1:
        if is_goal_stage(current_state):
            break
        elif current_state not in visited_states:
            visited_states.append(current_state)
            choices_of_move = get_choices(current_state)
            for p in range(0, len(choices_of_move)):
                choice = choices_of_move[p]
                new_position = choice[0]
                direction = choice[1]
                states_to_expand.push(new_position)
                path_to_current_state.push(path_to_goal + [direction])
        current_state = states_to_expand.pop()
        path_to_goal = path_to_current_state.pop()
    return path_to_goal


result = breadth_first_search()
for step in result:
    print(step)


