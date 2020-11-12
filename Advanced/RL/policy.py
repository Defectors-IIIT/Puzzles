import random

def greedy(state, ACTIONS, evaluation_function):
    best_action = ACTIONS[0]
    best_score = evaluation_function(state, best_action)
    for action in ACTIONS:
        if evaluation_function(state, action) > best_score:
            best_score = evaluation_function(state, action)
            best_action = action
    return best_action

def e_greedy(state, ACTIONS, evaluation_function, epsilon):
    choice_array = [0]*(int(1/epsilon))
    choice_array[0] = 1

    if random.choice(choice_array):
        return random.choice(ACTIONS)
    else:
        return greedy(state, ACTIONS, evaluation_function)

