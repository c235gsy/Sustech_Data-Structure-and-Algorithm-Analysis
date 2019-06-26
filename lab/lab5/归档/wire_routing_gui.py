from tkinter import *
import time


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


def state_value(state):
    return maze[state[0]][state[1]]


def get_choices(state):
    global lr, ld, ll, lu
    # Move order is: right, down, left, up
    choices = []
    x = state[0]
    y = state[1]
    score = state_value(state) + 1
    if y != 14 and maze[x][y+1] == 0 and (x, y+1) != get_start_stage():
        choices.append([(x, y+1), "right"])
        maze[x][y + 1] = score
        lr = Label(window, text=str(score), bg="MintCream", fg="black", width=1, height=1)
        lr.place(x=(y+1)*width+8, y=x*width+6)

    if x != 13 and maze[x+1][y] == 0 and (x+1, y) != get_start_stage():
        choices.append([(x+1, y), "down"])
        maze[x + 1][y] = score
        ld = Label (window, text=str (score), bg="MintCream", fg="black", width=1, height=1)
        ld.place (x=y * width+8, y=(x+1) * width+6)

    if y != 0 and maze[x][y-1] == 0 and (x, y-1) != get_start_stage():
        choices.append([(x, y-1), "left"])
        maze[x][y - 1] = score
        ll = Label (window, text=str (score), bg="MintCream", fg="black", width=1, height=1)
        ll.place (x=(y-1) * width+8, y=x * width+6)

    if x != 0 and maze[x-1][y] == 0 and (x-1, y) != get_start_stage():
        choices.append([(x-1, y), "up"])
        maze[x - 1][y] = score
        lu = Label (window, text=str (score), bg="MintCream", fg="black", width=1, height=1)
        lu.place(x=y * width+8, y=(x-1) * width+6)
    window.update_idletasks ()
    window.update ()
    time.sleep (0.01)
    return choices


def get_start_stage():
    return 13, 1


def get_goal_stage():
    return 11, 14


def is_goal_stage(stage):
    return stage == get_goal_stage()


def draw_mouse(state):
    x = state[0]
    y = state[1]
    view.create_rectangle (y * width, x * width, (y + 1) * width, (x + 1) * width, fill='yellow', outline='gray',
                           width=1)


def draw_visited(state):
    x = state[0]
    y = state[1]
    view.create_rectangle (y * width, x * width, (y + 1) * width, (x + 1) * width, fill='red', outline='gray', width=1)


def breadth_first_search():
    states_to_expand = Queue ()
    states_to_expand.push (get_start_stage())
    visited_states = []
    path_to_goal = []
    path_to_current_state = Queue ()
    current_state = states_to_expand.pop ()

    draw_mouse(current_state)
    view.pack ()
    window.update_idletasks ()
    window.update ()

    while True:
        if is_goal_stage(current_state):
            break
        elif current_state not in visited_states:
            visited_states.append(current_state)

            draw_visited(current_state)
            view.pack ()
            window.update_idletasks()
            window.update()
            time.sleep (0.02)

            choices_of_move = get_choices(current_state)
            for p in range(0, len(choices_of_move)):
                choice = choices_of_move[p]
                new_position = choice[0]
                states_to_expand.push(new_position)
                path_to_current_state.push(path_to_goal + [new_position])
        current_state = states_to_expand.pop()

        if current_state not in visited_states :
            draw_mouse (current_state)
            view.pack ()
            window.update_idletasks ()
            window.update ()
            time.sleep (0.02)
        path_to_goal = path_to_current_state.pop()
    for point in path_to_goal:
        draw_mouse (point)
        view.pack ()
        window.update_idletasks ()
        window.update ()
        time.sleep (0.02)

    return path_to_goal


global window, view
window = Tk()
window.title("Wire Routing")
width = 30
window.resizable(0, 0)
window.geometry("500x500")

for line in maze:
    print(line)

view = Canvas(window, width=column * width * 5, height=row * width * 5)
view.grid(row=0, column=0)

for x in range(row):
    for y in range(column):
        if maze[x][y] == 1:
            view.create_rectangle \
                (y * width, x * width, (y + 1) * width, (x + 1) * width, fill='black', outline='gray', width=1)
        else:
            view.create_rectangle \
                (y * width, x * width, (y + 1) * width, (x + 1) * width,fill='white', outline='gray', width=1)


start = get_start_stage()
p = start[0]
q = start[1]
view.create_rectangle(q * width, p * width, (q + 1) * width, (p + 1) * width, fill='blue', outline='gray', width=1)
goal = get_goal_stage()
m = goal[0]
n = goal[1]
view.create_rectangle(n * width, m * width, (n + 1) * width, (m + 1) * width, fill='green', outline='gray', width=1)
view.pack ()
window.update_idletasks ()
window.update ()
time.sleep(3)


result = breadth_first_search()
view.create_rectangle(n * width, m * width, (n + 1) * width, (m + 1) * width, fill='green', outline='gray', width=1)
view.create_rectangle(q * width, p * width, (q + 1) * width, (p + 1) * width, fill='blue', outline='gray', width=1)
for step in result:
    print(step)

view.pack()
window.mainloop()