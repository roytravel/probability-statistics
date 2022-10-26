import numpy as np

transition_matrix = np.atleast_2d([[0.7, 0.2, 0.1],
                                   [0.1, 0.6, 0.3],
                                   [0.2, 0.5, 0.3]])

possible_states = ["sunny", "rainy", "cloudy"]
start_state = "sunny"
num = 10
index_dict = {}
future_state = []

for index in range(len(possible_states)): # {'sunny': 0, 'rainy': 1, 'cloudy': 2}
    index_dict[possible_states[index]] = index

for _ in range(num):
    new_state = np.random.choice(possible_states, p=transition_matrix[index_dict[start_state], :])
    future_state.append(new_state)

print (future_state)