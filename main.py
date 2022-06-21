from Readfile import *
import pandas as pd
print('Hãy nhập vào địa chỉ file chứa Automaton: ')
link = input()
_states, _alphabet, _tran, _state_start, _state_final =  readFile(link)
ts = []
nut = ['a', 'b']
nfa = dict()
nfa1 = dict()
for i in range(len(_states)):
     print('Nhap di chuyen neu a cua nut %s' % _states[i])#dựa theo thông tin output
     val = [x for x in input().split()]
     ts.append(val)
     print('Nhap di chuyen neu b cua nut %s' % _states[i])
     val2 = [x for x in input().split()]
     ts.append(val2)
     nfa1 = dict(zip(nut, ts))
     ts.clear()
     nfa[_states[i]] = nfa1
print(nfa)
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())
nfa_final_state = _state_final  # Enter final state/states of NFA


new_states_list = []  # holds all the new states created in dfa
dfa = {}  # dfa dictionary/table or the output structure we needed
keys_list = list(list(nfa.keys())[0])
path_list = list(nfa[keys_list[0]].keys())  # list of all the paths eg: [a,b] or [0,1]

###################################################

# Computing first row of DFA transition table

dfa[keys_list[0]] = {}  # creating a nested dictionary in dfa
for y in range(2):
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])  # creating a single string from all the elements of the list which is a new state
    dfa[keys_list[0]][path_list[y]] = var  # assigning the state in DFA table
    if var not in keys_list:  # if the state is newly created
        new_states_list.append(var)  # then append it to the new_states_list
        keys_list.append(var)  # as well as to the keys_list which contains all the states

###################################################

# Computing the other rows of DFA transition table

while len(new_states_list) != 0:  # consition is true only if the new_states_list is not empty
    dfa[new_states_list[0]] = {}  # taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []  # creating a temporay list
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  # taking the union of the states
            s = ""
            s = s.join(temp)  # creating a single string(new state) from all the elements of the list
            if s not in keys_list:  # if the state is newly created
                new_states_list.append(s)  # then append it to the new_states_list
                keys_list.append(s)  # as well as to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s  # assigning the new state in the DFA table

    new_states_list.remove(new_states_list[0])  # Removing the first element in the new_states_list

print("\nDFA :- \n")
print(dfa)  # Printing the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)

