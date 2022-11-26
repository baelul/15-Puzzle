import copy
from priorityQueue import *

## Calculate Chessboard Distance of Entire Board
def chessboardDistance(w, curr_state, goal_state):
    # for every element in curr_state, run through goal_state and find its position.
    # once found - calculate moves needed to get to goal (X and Y distances), find the max,
    # add it to the mDist sum, and then break loop
    # this will repeat for every element in curr_state (i)
    
    # structure
    # curr: [[x,x,x,x],
    #        [x,x,x,x],
    #        [x,x,x,x],
    #        [x,x,x,x]]

    # goal: [[x,x,x,x],
    #        [x,x,x,x],
    #        [x,x,x,x],
    #        [x,x,x,x]]
    
    mDist = 0
    
    for curr_y in range(4):
        for curr_x in range(4):
            distX = 0
            distY = 0
            
            # zero is the empty space, there is no h(n) for this value
            if (curr_state[curr_y][curr_x] == '0'):
                continue

            for goal_y in range(4):
                for goal_x in range(4):
                    # if goal value matches current element, compare locations
                    if (curr_state[curr_y][curr_x] == goal_state[goal_y][goal_x]):
                        distX = abs(curr_x - goal_x) # X distance (L or R moves needed)
                        distY = abs(curr_y - goal_y) # Y distance (U or D moves needed)
                        mDist += max(distX, distY)
    return w * mDist
    
## Return state after a certain move is made
def board_after_move(state, move, x, y):
    nxt_state = copy.deepcopy(state)

    # [x, 0] -> [0, x]
    if (move == 'L'):
        temp = nxt_state[y][x]
        nxt_state[y][x] = nxt_state[y][x - 1] # [x, 0] -> [x, x]
        nxt_state[y][x - 1] = temp                      # [x, x] -> [0, x]
            
    # [0, x]  -> [x, 0]
    elif (move == 'R'):
        temp = nxt_state[y][x]
        nxt_state[y][x] = nxt_state[y][x + 1] # [x, 0] -> [x, x]
        nxt_state[y][x + 1] = temp                      # [x, x] -> [0, x]
            
    # [0] -> [x]
    # [x]    [0]
    elif (move == 'D'):
        temp = nxt_state[y][x]
        nxt_state[y][x] = nxt_state[y + 1][x]
        nxt_state[y + 1][x] = temp

    # [x] -> [0]
    # [0]    [x]
    elif (move == 'U'):
        temp = nxt_state[y][x]
        nxt_state[y][x] = nxt_state[y - 1][x]
        nxt_state[y - 1][x] = temp
        
    return nxt_state
    
    
## Expand a node, returning reachable children
def expand(node):
    moves = ['L', 'R', 'U', 'D']
    for move in moves:
        parent = copy.deepcopy(node)
        x, y = 0, 0
        for row in range(4):
            for col in range(4):
                if (parent.state[row][col] == '0'):
                    x,y = col, row
        
        not_reachable = ((move == 'L' and x == 0) or (move == 'R' and x == 3) or (move == 'U' and y == 0) or (move == 'D' and y == 3))
                    
        if not_reachable:
            continue
            
        child_state = board_after_move(parent.state, move, x, y)
        child_g = node.g + 1
        
        yield Node(child_state, node, child_g, move)


## Weighted A* Search Implementation -> f(n) = g(n) + w * h(n)
def weightedAStarSearch(w, initial_state, goal_state):
    frontier = PriorityQueue()
    already_seen = PriorityQueue()
    
    # create initial node
    node = Node(initial_state, None, 0)
    node.h = chessboardDistance(w, initial_state, goal_state) # make sure to add weight
    node.f = node.g + node.h # for initial node, g is 0 so f(n) = h(n)
    
    frontier.push(node)
    already_seen.push(node)
    
    # while frontier is not empty, run the algorithm
    while not frontier.isEmpty():
        node = frontier.pop_min()
        
        # if node has reached goal, return
        if node.state == goal_state:
            curr = node
            d = 0  # depth
            f = [] # f(n) values
            A = [] # moves made
            
            while curr.parent is not None:
                if curr.move is not None:
                    A.append(curr.move)
                f.append(round(curr.f, 1))
                d += 1
                curr = curr.parent
            f.append(round(curr.f, 1))
            A.reverse()
            f.reverse()
            return A, d, len(already_seen.queue), f
            
        for child in expand(node):
            if child not in already_seen.queue:
                child.h = chessboardDistance(w, child.state, goal_state)
                child.f = child.g + child.h
                already_seen.push(child)
                frontier.push(child)
                
    return ['fail'], ['fail'], ['fail'], ['fail']
