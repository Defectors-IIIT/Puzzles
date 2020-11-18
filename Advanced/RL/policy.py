def greedy(state, actions, evaluation_function):
    best_action = actions[0]
    best_score = evaluation_function(state, best_action)
    for action in actions:
        if evaluation_function(state, action) > best_score:
            best_score = evaluation_function(state, action)
            best_action = action
    return best_action
