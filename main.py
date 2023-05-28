"""
Asala Ehab

"""

import numpy as np

def is_periodic(pij):
    eigenvalues = np.linalg.eigvals(pij)
    if all(abs(eigenvalues[0]) - abs(val) < 1e-8 for val in eigenvalues):
        print("Markov chain is periodic")
    else:
        print("Markov chain is aperiodic")
def is_reducible(pij):
    n = 100
    raised_matrix = np.linalg.matrix_power(pij, n)
    if np.all(raised_matrix > 0):
        print("Markov chain is irreducible")
    else:
        print("Markov chain is reducible")

def is_absorbing(pij):
    absorbing_states = np.diag(pij) == 1
    if np.any(absorbing_states):
        print("Markov chain is absorbing")
    else:
        print("Markov chain is not absorbing")
def is_close(pij):
    n = 100
    raised_matrix = np.linalg.matrix_power(pij, n)
    closed_set = np.any(np.all(raised_matrix > 0, axis=1))
    if closed_set:
        print("Markov chain has a closed set")
    else:
        print("Markov chain does not have a closed set")



def state_reachable(Pij,num_states):
    reachable_states = np.zeros(num_states, dtype=bool)
    pij=np.array(Pij)
    reachable_states_final=[]
    for row_idx in range(num_states):
        if np.sum(pij[row_idx, :]) > 0:
            reachable_states[row_idx] = True
    for state_idx, reachable in enumerate(reachable_states):
        if reachable:
            reachable_states_final.append("reachable")
        else:
            reachable_states_final.append("not reachable")
    return reachable_states_final

def state_absorbing(Pij,num_states):
    absorbing_state=[]
    absorbing_state_final=[]
    pij = np.array(Pij)
    for state_idx in range(num_states):
        is_absorbing = np.any(pij[state_idx, state_idx] == 1)
        absorbing_state.append(is_absorbing)
    for state_idx, is_abs in enumerate(absorbing_state):
        if is_abs:
            absorbing_state_final.append("absorbing")
        else:
            absorbing_state_final.append("not absorbing")
    return absorbing_state_final

def state_transient(pij,num_states):
    transient_states = [True] * num_states
    transient_states_final=[]
    for state_idx in range(num_states):
        for j in range(num_states):
            if pij[i][j]>0:
                transient_states[state_idx] = False
                break
    for state_idx, transient in enumerate(transient_states):
        if transient:
            transient_states_final.append("transient")
        else:
            transient_states_final.append("not transient")
    return transient_states_final

def state_recurrent(Pij,num_states):
    recurrent_states = []
    recurrent_states_final=[]
    pij = np.array(Pij)
    for state_idx in range(num_states):
        is_recurrent = np.any(pij[state_idx, state_idx] > 0)
        recurrent_states.append(is_recurrent)
    for state_idx, is_recurrent in enumerate(recurrent_states):
        if is_recurrent:
            recurrent_states_final.append(" recurrent")
        else:
            recurrent_states_final.append(" not recurrent")
    return recurrent_states_final


num_rows = int(input("Enter the number of states: "))
Pij = []
for i in range(num_rows):
    row = []
    for j in range(num_rows):

        element = float(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    Pij.append(row)


n = int(input("Enter the number of initial : "))
initial_vector = []
for i in range(n):
    num = float(input())
    initial_vector.append(num)


numOfSteps = int(input("Enter the number of the steps: "))
states_Id = []
for i in range(num_rows):
    stat = int(input(f"Enter state_ID {i} : "))
    states_Id.append(stat)


is_periodic(Pij)
is_reducible(Pij)
is_absorbing(Pij)
is_close(Pij)

print("********************************************************************************************")

reachability = state_reachable(Pij, num_rows)
recurrently = state_recurrent(Pij, num_rows)
transient = state_transient(Pij, num_rows)
absorb = state_absorbing(Pij, num_rows)
for j in range(num_rows):
    print(f"state ({j+1}) with id  ", states_Id[j], reachability[j], " ", recurrently[j], " ",transient[j], " ", absorb[j])


print("***********************************************************************************************\n")
result = np.dot(initial_vector, Pij)
print("State Transition Probabilities\n", result)
print("***********************************************************************************************\n")

state_vector_after_steps = np.linalg.matrix_power(Pij, numOfSteps)
print(f"State Probabilities after {numOfSteps} Steps\n", state_vector_after_steps)

